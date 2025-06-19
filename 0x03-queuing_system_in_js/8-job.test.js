import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  // Set up the queue and enter test mode before tests
  before(() => {
    queue = kue.createQueue({
      redis: {
        host: '127.0.0.1',
        port: 6379,
      },
    });
    queue.testMode.enter();
  });

  // Clear the queue and exit test mode after tests
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs(123, queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
