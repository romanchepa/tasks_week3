from datetime import datetime, timedelta

dt_now = datetime.now()
dt_now.strftime('%d. %m. %Y %H:%M')
print(dt_now)


delta = timedelta(days=1)
dt_yesterday = dt_now - delta
print (dt_yesterday)


delta30 = timedelta(days=30)
dt_30 = dt_now - delta30
print(dt_30)


date_string = "01/01/25 12:10:03.234567"
date_dt = datetime.strptime(date_string, "%y/%m/%d %H:%M:%S.%f")
print(date_dt)
