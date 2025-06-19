import redis from 'redis';

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});

// Handle connection success
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Store hash values using hset
client.hset('ALX', 'Portland', '50', redis.print);
client.hset('ALX', 'Seattle', '80', redis.print);
client.hset('ALX', 'New York', '20', redis.print);
client.hset('ALX', 'Bogota', '20', redis.print);
client.hset('ALX', 'Cali', '40', redis.print);
client.hset('ALX', 'Paris', '2', redis.print);

// Display the hash using hgetall
client.hgetall('ALX', (err, reply) => {
  if (err) {
    console.error(`Error retrieving hash: ${err.message}`);
    return;
  }
  console.log(reply);
});
