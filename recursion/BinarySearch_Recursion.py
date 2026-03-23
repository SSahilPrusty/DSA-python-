# BINARY SEARCH USING THE RECURSION
def binarysearch(arr,low,high,target):
    if(low>high):
        return -1
    mid=(low+high)//2
    if (arr[mid]==target):
        return mid
    elif(arr[mid]>target):
       return binarysearch(arr,low,mid-1,target)
    else:
       return  binarysearch(arr,mid+1,high,target)

arr = [1, 3, 5, 7, 9]
print(binarysearch(arr, 0, len(arr)-1, 7))     