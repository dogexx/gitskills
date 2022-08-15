import sys
import time

time_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(time_now)
sys.exit()

print(time.strptime(time_now, '%Y/%m/%d'))
