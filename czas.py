import time
import calendar as cal

print(cal.calendar(2023))
print(cal.firstweekday())
print(cal.month(2421, 12))

local_time = time.ctime()
# time.sleep(2)
print(local_time)
result = time.localtime()
print(result)
print(result.tm_year)
print(result.tm_hour)

t = (2018, 12, 28, 8, 32, 2, 4, 362, 0)
local = time.mktime(t)
local2 = time.asctime(t)
print(local)
print(local2)

time_string = time.strftime("%Y--%m--%d", result)
print(time_string)
