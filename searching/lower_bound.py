'''A lower bound is the minimum possible value within a set, function, or range, 
representing a constraint that no value in that set falls below'''
#---------------------linear search-----------------------------
def lower_bound(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] >= x:
            return i
    return n   

print("linear search")
arr = [10,12,13,40,50,69,77,89,90]
p = lower_bound(arr, 70)
print(p)

#-----------------------binary  search-------------------------
def lower_bound_b(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n   # default (if no element >= x)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid        # possible answer
            high = mid - 1   # look left for smaller index
        else:
            low = mid + 1    # go right

    return ans
       

print("binary search")
arr = [10,12,13,40,50,69,77,89,90]
p = lower_bound_b(arr, 70)
print(p)
