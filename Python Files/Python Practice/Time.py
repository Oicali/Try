'''
import time

seconds = time.time()
print("Time in seconds since the epoch:", seconds)
local_time = time.ctime(seconds)
print("Local time:", local_time)
'''

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

print("Current Time is :", current_time)