from apscheduler.schedulers.blocking import Blockingscheduler
sched = Blockingscheduler()
@sched.scheduled_job('interval',minutes = 30)
def timed_job():
    print('done')
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()    