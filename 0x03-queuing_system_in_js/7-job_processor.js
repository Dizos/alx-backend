import kue from 'kue';

// Blacklist of phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a Kue queue
const queue = kue.createQueue({
  redis: {
    host: '127.0.0.1',
    port: 6379,
  },
});

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track progress at 0%
  job.progress(0, 100);

  // Check if phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress at 50%
  job.progress(50, 100);

  // Log notification message
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
}

// Process jobs in push_notification_code_2 queue, up to 2 at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
