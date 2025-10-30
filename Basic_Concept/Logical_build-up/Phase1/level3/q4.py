# Take a password string and check basic rules (length ≥ 8 and contains at least one digit). 

password = input("Enter your password: ")
if len(password) > 8:
    print("Your Password is Valid")
else:
    print("Your Password is not Valid")