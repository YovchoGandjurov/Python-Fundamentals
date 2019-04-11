import datetime

data = input().split("-")
year = int(data[0])
month = int(data[1])
day = int(data[2])

today = datetime.date.today()
curr_date = datetime.date(year, month, day)
result = curr_date - today


if int(result.days) < 0:
    print("Passed")
elif int(result.days) == 0:
    print("Today date")
else:
    print(f"{result.days + 1} days left")