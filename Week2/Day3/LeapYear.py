
def is_leap_year(year):
    is_leap = False
    if year % 4 == 0:
        is_leap = True
        if year % 100 == 0:
            is_leap = False
            if year % 400 == 0:
                is_leap = True
    return is_leap

year = int(input("Enter the year: "))
print(is_leap_year(year))