import calendar
c = calendar.Calendar(6)

days = []
for i in c.iterweekdays():
    days.append(calendar.day_name[i])

months = []
short_months = []
iteration = 0
for i in calendar.month_name:
    if i != "":
        months.append(i)
    if iteration == 4 or iteration == 6 or iteration == 9 or iteration == 11:
        short_months.append(i)
    iteration += 1


doomsdays = [3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]
leapdooms = [4, 29]

def leap_year(y):
    return y % 100 and not y % 4 or not y % 400

def length_of_month(m, y):
    if m == "February":
        if leap_year(y):
            return 29
        return 28
    if m in short_months:
        return 30
    return 31

def get_year():
    try:
        return int(input("year : "))
    except:
        print("invalid year")
        return get_year()

def get_month():
    month = ""
    while (not month in months):
        month = input("month : ")
    return month

def get_day(m, y):
    try:
        day = int(input("day : "))
        if day > length_of_month(m, y):
            print("invalid day (too long)")
            return get_day(m, y)
        else:
            return day
    except:
        print("invalid day (must be a number)")
        return get_day(m, y)

def anchor(y):
    c = y // 100
    a = 5 * (c % 4) % 7 + 2
    return a

def find_doomsday(y, a):
    return ((y//12) + y % 12 + ((y % 12)// 4)) % 7 + a - 8

def find_weekday(y, m, d, l):
    doomsdate = doomsdays[months.index(m)]
    if l and (m == "January" or m == "February"):
        doomsdate = leapdooms[months.index(m)]
    r = (d - doomsdate) % 7
    return days[doomsday + r]

year = get_year()
is_leap = leap_year(year)
month = get_month()
day = get_day(month, year)
doomsday = find_doomsday(year, anchor(year))

print(f"The {day} of {month} {year} is {find_weekday(year, month, day, is_leap)}")

days[find_doomsday(year, anchor(year))]