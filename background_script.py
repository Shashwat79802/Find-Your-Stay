import datetime
import pytz
from FindYourStay.job import the_job
import time


while True:

    timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now().strftime("%H:%M")
    # print(current_time)
    if (current_time == "11:10"):
        the_job()
    time.sleep(1)
