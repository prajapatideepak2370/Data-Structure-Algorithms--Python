# Take electricity units consumed and calculate the bill as per slabs (using if-else). 
elec = int(input("Enter the units consumed: "))
consumed_bill = 0

if elec <= 100: # --- 100 unit or less then 100 unit
    consumed_bill = elec*5
elif elec > 101 and elec <= 200:
    consumed_bill = (100*5) + ((elec - 100)*7)
else:
    consumed_bill = (100*5) + (100*7) + ((elec - 200) *10)

print("The Total consumed electricity Bill: ", consumed_bill)