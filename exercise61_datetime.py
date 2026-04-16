import datetime

date = datetime.date(2025,1,2)
print(date)

today_date = datetime.date.today()
print(today_date)

time = datetime.time(12,30,0)
print(time)

current_time = datetime.datetime.now()
current_time = current_time.strftime("%H:%M:%S %d-%m-%Y")
print(current_time)

target_datetime = datetime.datetime(2029,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if current_datetime < target_datetime:
    print("Target date has NOT passed")
else:
    print("Target date has passed")