# Approach : Using extend() and sort()

# First copy the given array into two different arrays using extend()
# Sort the first array in ascending order using sort()
# Sort the second array in descending order using sort(reverse=True)
# If the given array is equal to any of the two arrays then the array is monotonic

def array_is_monotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True
    return False
 
 

A = [6, 5, 4, 4]
 
print(array_is_monotonic(A))