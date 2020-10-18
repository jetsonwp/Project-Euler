# 1 Jan 1901 was a Tuesday
startYear = 1901
endYear = 2001
year = 1901
month = 0
monthName = ""
date = 0
day = 2
# number of days for any given month
days = 30
# number of Sundays that fell on the first of the month
sundayCount = 0
# If the value of leap is 0 it is not a leap year if it is 1 it is a leap year
leap = 0
for e in range(startYear, endYear):
    # checks for leap years
    if year % 4 == 0 and year % 100 != 0:
        leap = 1
    elif year % 400 == 0:
        leap = 1
    elif year % 100 == 0:
        leap = 0
    else:
        leap = 0
    # cycles through the months, Checks for how many days,
    for q in range(12):
        month += 1
        if month == 1:
            days = 31
            monthName = "Jan"
        if month == 2:
            monthName = "Feb"
            if leap == 1:
                days = 29
            else:
                days = 28
        if month == 3:
            monthName = "Mar"
            days = 31
        if month == 4:
            monthName = "Apr"
            days = 30
        if month == 5:
            monthName = "May"
            days = 31
        if month == 6:
            monthName = "Jun"
            days = 30
        if month == 7:
            monthName = "Jul"
            days = 31
        if month == 8:
            monthName = "Aug"
            days = 31
        if month == 9:
            monthName = "Sep"
            days = 30
        if month == 10:
            monthName = "Oct"
            days = 31
        if month == 11:
            monthName = "Nov"
            days = 30
        if month == 12:
            monthName = "Dec"
            days = 31
        # Cycles through the days, Prints out the name of the month, the date, the day, and the year
        for i in range(days):
            date += 1
            day += 1
            print(monthName, "/", date, "Day: ", day, "Year: ", year)
            if day == 7:
                day = 0
            # checks to see if it was a sunday on the first day of each month
            if date == 1 and day == 1:
                sundayCount += 1
        # resets the date at the end of each month
        date = 0
    # increases the year
    year += 1
print(sundayCount)
