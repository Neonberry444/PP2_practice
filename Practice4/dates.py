# #1.
# import datetime
# x = datetime.datetime.now()
# y = x - datetime.timedelta(days=5)
# print(y.strftime("%Y-%m-%d"))

#2.
import datetime
x = datetime.datetime.now()
yesterday = x - datetime.timedelta(days=1)
today = x
tomorrow = x + datetime.timedelta(days=1)
print(yesterday.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

# #3.
# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%Y-%m-%d %H:%M:%S"))

# #4.
# import datetime
# x = datetime.datetime(2026, 2, 28, 11, 44, 23)
# y = datetime.datetime(2026, 2, 14, 11, 44, 21)
# dif = x - y
# print(dif.total_seconds())