import redis from 'redis';

// Create a Redis client
const publisher = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});

// Handle connection success
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish a message after a delay
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('ALXchannel', message);
  }, time);
}

// Publish messages with specified delays
publishMessage('ALX Student #1 starts course', 100);
publishMessage('ALX Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('ALX Student #3 starts course', 400);
