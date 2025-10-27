# Take three sides and check if they form a valid triangle.
s1 = int(input("Enter the Side one: "))
s2 = int(input("Enter the Side two: "))
s3 = int(input("Enter the Side three: "))

if (s1 + s2 > s3):
    if(s2 + s3 > s1):
        if(s1 + s3 > s2):
                print("The sides form a VALID TRIANGLE.")
        else:
            print("The sides DO NOT form a valid triangle.")
    else:
        print("The sides DO NOT form a valid triangle.")
else:
    print("The sides DO NOT form a valid triangle.")
