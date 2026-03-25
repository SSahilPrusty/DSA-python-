"""Quick Sort is a divide-and-conquer sorting algorithm in which we choose
a pivot element (usually the last element), 
rearrange the array so that all smaller elements come
before the pivot and all larger elements come after it,
place the pivot in its correct position using the partition function,
and then recursively apply the same process to the left and right 
subarrays until the entire array is sorted, with an average time complexity of O(n log n).
"""
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range (low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1 

def quick_sort(arr,low,high):
    if low<high:
      pi=partition(arr,low,high)
      quick_sort(arr,low,pi-1)
      quick_sort(arr,pi+1,high)   



arr=[1,5,3,8,9,2,63,23]
quick_sort(arr,0,len(arr)-1)
print(arr)

#unstable sort