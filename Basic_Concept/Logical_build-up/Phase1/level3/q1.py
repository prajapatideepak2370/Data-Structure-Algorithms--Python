# Take a character and check if it is a letter, a digit, or neither. 
x = input("Enter character: ")
if x.isalpha():
    print("Its is a Letter")
elif x.isdigit():
    print("Its is Integer")
else:
    print("Neither")
