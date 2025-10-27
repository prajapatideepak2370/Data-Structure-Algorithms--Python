# Check if a given year is a leap year.

year  = int(input("Enter the year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("THIS IS A LEAP YEAR")

else:
    print("THIS IS NOT A LEAP YEAR")