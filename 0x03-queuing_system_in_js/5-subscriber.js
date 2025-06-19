import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});

// Handle connection success
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to ALXchannel
subscriber.subscribe('ALXchannel');

// Handle messages on ALXchannel
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('ALXchannel');
    subscriber.quit();
  }
});
