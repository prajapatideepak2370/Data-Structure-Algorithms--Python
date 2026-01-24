# Combination Problem

def nCr_Sol(n, r):
    result = 1
    for i in range(0, r):
        result *= (n-i)
        result = result/(i+1) 
    return result
print("Answer :- ", nCr_Sol(10, 3))