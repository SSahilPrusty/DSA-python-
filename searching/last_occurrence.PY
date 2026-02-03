'''1. Last Occurrence of an Element
Given a sorted array of n elements and a target x.
Find the last occurrence of x in the array. 
If x does not exist, return -1.

Input 1: arr[] = {1,2,3,3,4,4,4,5}, x = 4  
Output 1: 6
'''

def last_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            ans = mid          # store index
            low = mid + 1      # move right to find last occurrence
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return ans


arr = [1,2,3,3,4,4,4,5]
x = 4
print(last_occurrence(arr, x))
