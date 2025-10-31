# Take day and month and check if it forms a valid calendar date (ignoring leap years).

date = int(input("Enter the Date: "))
month = int(input("Enter the Month: "))

if date <= 31:
    if month <= 12:
        print("It forms a Valid Calender date")
else:
    print("Invalid Calender Date")