import random
from apscheduler.schedulers.blocking import BlockingScheduler
import zoneinfo
from flask import request
import urllib.request
from PIL import Image
from coreModule import executeData

JKT = zoneinfo.ZoneInfo("Asia/Jakarta")
sched = BlockingScheduler(timezone=JKT)

def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")

def schedule():
    print('starting') 
    i = 0
    for i in range(1):
        x = random.randint(0, 59)
        print(x)
        sched.add_job(executeData.uploadImage, 'cron', second='*')
        print(executeData.uploadImage())
    # sched.add_job(executeData.uploadImage, 'cron', hour=16, minute=40, jitter=30)  
        
    sched.start()
    # print(executeData.uploadImage())

