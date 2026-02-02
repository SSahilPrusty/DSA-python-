def binary_search(arr,x):
    n=len(arr)
    low=0
    high=n
    while low<=high :
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x :
            high-=1
        else:
            low+=1    



arr=[1,2,3,4,5,6,7,8,9,10]
p=binary_search(arr,7)
print(p)            