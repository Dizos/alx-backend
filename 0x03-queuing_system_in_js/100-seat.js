import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

// Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379,
});
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize available seats and reservation status
let reservationEnabled = true;

// Function to reserve seats
function reserveSeat(number) {
  return setAsync('available_seats', number);
}

// Function to get current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats !== null ? parseInt(seats, 10) : 0;
}

// Initialize available seats to 50
reserveSeat(50);

// Kue queue
const queue = kue.createQueue({
  redis: {
    host: '127.0.0.1',
    port: 6379,
  },
});

// Express server
const app = express();
const port = 1245;

// Route: Get available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

// Route: Reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

// Route: Process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      const currentSeats = await getCurrentAvailableSeats();
      if (currentSeats <= 0) {
        reservationEnabled = false;
        throw new Error('Not enough seats available');
      }

      await reserveSeat(currentSeats - 1);
      const newSeats = await getCurrentAvailableSeats();

      if (newSeats === 0) {
        reservationEnabled = false;
      }

      done();
    } catch (err) {
      done(err);
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
