import kue from 'kue';

// Function to create push notification jobs
function createPushNotificationsJobs(jobs, queue) {
  // Validate that jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate through jobs and create a job for each
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    // Handle job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Handle job failure
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // Handle job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
