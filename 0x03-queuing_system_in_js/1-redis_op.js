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

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a school key
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving ${schoolName}: ${err.message}`);
      return;
    }
    console.log(reply);
  });
}

// Execute the required operations
displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
