## 1. The Time Module ##

import time
current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
current_year = current_struct_time.tm_year
current_day = current_struct_time.tm_mday
current_month = current_struct_time.tm_mon
print(current_time, current_hour, current_year, current_month, current_day)

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month
print(current_datetime)
print(current_year)
print(current_month)

## 4. Timedelta ##

import datetime
kirks_birthday = datetime.datetime(year=2233, month=3, day=22)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff
print(before_kirk)

## 5. Formatting Dates ##

import datetime
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime
mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date)

## 8. Reformatting Our Data ##

import datetime
for each in posts :
    each[2] = datetime.datetime.fromtimestamp(float(each[2]))
    each

## 9. Counting Posts from March ##

march_count = 0
for each in posts :
    if each[2].month == 3:
        march_count += 1
print(march_count)

## 10. Counting Posts from Any Month ##

march_count = 0
def month_count(month) :
    count = 0
    for row in posts:
        if row[2].month == month:
            count += 1
    return count
feb_count = month_count(2)
print(feb_count)
aug_count = month_count(8)
print(aug_count)