
#
# x = datetime.datetime.now()
# print(x)
#
# x = datetime.datetime.now()
#
# print(x.year)
# print(x.strftime("%A"))
#
# x = datetime.datetime(2020, 5, 17)
#
# print(x)
#
# x = datetime.datetime(2018, 6, 1)
#
# print(x.strftime("%B"))

# # Function to convert string to datetime
# def convert(date_time):
# 	format = '%b %d %Y %I:%M%p' # The format
# 	datetime_str = datetime.datetime.strptime(date_time, format)
# 	return datetime_str
#
# # Driver code
# date_time = 'Dec 4 2018 10:07AM'e
# print(convert(date_time))

# Date=datetime.datetime.strftime('2016,3,1 10:07AM')
# print(Date)
# print(Date.strftime('%b'))


# from datetime import date,datetime, timedelta
# date=datetime.now()-timedelta(days=5)
# mydate=date.today()
# mydatetime=datetime(mydate.year,mydate.month,mydate.day)
# print(mydatetime)

from datetime import date,datetime,timedelta
myday=date.today()
mytime=datetime.min.time()
mydatetime=datetime.combine(myday,mytime)
print(mydatetime)
mydate=datetime.today()
for x in range(0,5):
    print(mydate+timedelta(days=x))

base = datetime.today()
for x in range(0, 5):
    print(base +`timedelta(days=x))

from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)
