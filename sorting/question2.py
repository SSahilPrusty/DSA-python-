"""Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in sorted order, not the kth distinct element.

📥 Example 1
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
📥 Example 2
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4"""



#bubble sort
def bubble_sort(arr,k):
    n=len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
   
    return arr[n-k] 




nums=[3,2,1,5,6,4]
n=bubble_sort(nums,2)
print(n)




#selection sort

def selection_sort(arr,k):
    for i in range(0,len(arr)):
        min_index=i
        for j in range (i+1, len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
            arr[j],arr[min_index]=arr[j],arr[min_index]

    return arr[n-k]


nums=[3,2,1,5,6,4]
n=selection_sort(nums,2)
print(n)
