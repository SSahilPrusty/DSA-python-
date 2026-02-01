'''Insertion sort is a simple, in-place, stable sorting algorithm that builds a final sorted array one element at a time'''
def inseration_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr



arr=[9,8,7,6,5,4,3,2,1,0]
print("the unsorted arry:-",arr)
inseration_sort(arr)
print("the sorted array:-",arr)