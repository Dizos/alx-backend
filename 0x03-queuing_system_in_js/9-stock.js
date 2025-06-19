import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Product list
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Function to get item by ID
function getItemById(id) {
  return listProducts.find((item) => item.id === parseInt(id, 10));
}

// Create Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});

// Promisify Redis get and set
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to reserve stock by ID
function reserveStockById(itemId, stock) {
  return setAsync(`item.${itemId}`, stock);
}

// Async function to get current reserved stock by ID
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock, 10) : 0;
}

// Create Express server
const app = express();
const port = 1245;

// Route: List all products
app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map((item) => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  }));
  res.json(formattedProducts);
});

// Route: Get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const availableStock = item.stock - currentStock;

  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: availableStock,
  });
});

// Route: Reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const availableStock = item.stock - currentStock;

  if (availableStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: parseInt(itemId, 10) });
  }

  await reserveStockById(itemId, currentStock + 1);
  res.json({ status: 'Reservation confirmed', itemId: parseInt(itemId, 10) });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
