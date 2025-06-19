import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue({
  redis: {
    host: '127.0.0.1',
    port: 6379,
  },
});

// Function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in the push_notification_code queue
queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
