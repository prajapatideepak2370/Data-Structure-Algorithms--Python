#Take a character and check whether it’s uppercase, lowercase, a digit, or a special character. 

ch = input("Enter a single character: ")

if len(ch) == 1:  # Make sure only one character is entered
    if ch.isupper():
        print("It is an UPPERCASE letter.")
    elif ch.islower():
        print("It is a LOWERCASE letter.")
    elif ch.isdigit():
        print("It is a DIGIT.")
    else:
        print("It is a SPECIAL CHARACTER.")
else:
    print("Please enter only one character.")
