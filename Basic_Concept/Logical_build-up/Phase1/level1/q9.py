#  Take a character and check if it’s a vowel or consonant. 
ch = input("Enter the character: ").lower()
if len(ch) == 1 and ch.isalpha():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("VOWEL")
    else:
        print("CONSONANT")
else:
    print("Please enter a valid single alphabet character.")