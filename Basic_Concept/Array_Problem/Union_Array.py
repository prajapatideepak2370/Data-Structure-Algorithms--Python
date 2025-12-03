arr1 = [1,1,2,3,4,4,4,5]         # N1
arr2 = [2,2,3,3,4,5,5,6,6,7,7]   # N2

# Brute Force Approach
def union_A(arr1, arr2):
    st = set()
    for i in range(len(arr1)):   # TC = O(N1 LOG N)
        st.add(arr1[i]) 

    for j in range(len(arr2)):   # TC = O(N2 LOG N)
        st.add(arr2[j])
    
    union = []
    for it in st:                # TC = O(N1 + N2)
        union.append(it)
    return union

print(union_A(arr1, arr2))
"""Time Complexity = O(N1 LOG N + N2 LOG N) + O(N1 + N2)
    Space Complexity = O(N1 + N2) + O(N1+N2)---> return the union array """