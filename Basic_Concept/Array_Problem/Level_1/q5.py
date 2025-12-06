#Count how many elements are positive, negative, or zero

arr = [2,3,4,5,0,1,7,8,6,-1,0,0,-5,-2]

pos = neg = zr = 0
for num in arr:
    if num < 0:
        neg +=1
    elif num == 0:
        zr += 1
    else:
        pos +=1
print(neg, pos, zr)