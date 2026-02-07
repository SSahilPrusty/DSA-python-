'''Given a sorted binary array, efficiently count the total number of 1’s in it.

Input 1: a = [0,0,0,0,1,1]  
Output 1: 2'''

def count_ones(arr):
    n = len(arr)
    low, high = 0, n - 1
    first_one = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == 1:
            first_one = mid
            high = mid - 1   # search left
        else:
            low = mid + 1    # search right

    if first_one == -1:
        return 0  # no 1s present

    return n - first_one


# Example
a = [0,0,0,0,1,1]
print(count_ones(a))
