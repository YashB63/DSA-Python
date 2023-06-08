# Algorithm

# Initialize an array.
# Sort the array in ascending order.
# The first element of the array will be the minimum element.
# The last element of the array will be the maximum element.
# Print the minimum and maximum element.

def get_minimum_maximum(arr):
    arr.sort()
    minimum_maximum = {"min": arr[0], "max": arr[-1]}
    return minimum_maximum

arr = [20, 10, 40, 63, 32, 71]
minimum_maximum = get_minimum_maximum(arr)

print("Minimum element in the array is: ", minimum_maximum["min"])
print("Maximum element in the array is: ", minimum_maximum["max"])

# Time Complexity: O(nlogn)
# Space Complexity: O(1)