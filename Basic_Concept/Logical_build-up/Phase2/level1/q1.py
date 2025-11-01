# Print all even numbers between 1 and 100.

n = 100 
print('All even numbers between 1 and 100.')
for i in range(1, 100):
    if i % 2 == 0:
        print(i)
    i += 1

# Print all Odd numbers between 1 and 100
print()
print("All Odd numbers between 1 and 100.")

for i in range(1, 100):
    if i % 2 != 0:
        print(i)
    i += 1


#Print numbers from 10 down to 1.
for i in range(10, 0, -1):
    print(i)
