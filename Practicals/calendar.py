def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year, month):
    
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28

def get_start_day(year, month):
    
    if month < 3:
        month += 12
        year -= 1
    
    k = year % 100  
    j = year // 100  
    
    h = (1 + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7 #Zeller's congruence

    
    return (h + 5) % 7

def display_month(year, month):
    
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    
    print(f"\n{'='*10} {month_names[month - 1]} {year} {'='*10}")
    print(" ".join(days))  

    
    start_day = get_start_day(year, month)
    days_in_month = get_days_in_month(year, month)

    
    print("   " * start_day, end="")  
    for day in range(1, days_in_month + 1):
        print(f"{day:2} ", end="")
        if (start_day + day) % 7 == 0:  
            print()
    print("\n" + "-"*30)

def display_year_calendar(year):
    
    for month in range(1, 13):
        display_month(year, month)


try:
    year = int(input("Enter the year for the calendar: "))
    display_year_calendar(year)
except ValueError:
    print("Please enter a valid year.")
