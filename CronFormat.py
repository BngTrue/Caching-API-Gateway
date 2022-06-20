from crontab import CronTab

my_cron = CronTab(user='roy')
job = my_cron.new(command='python /home/project/main.py')
job.minute.every(1)

my_cron.write()