'''The peak index in a mountain array is the index \(i\) of the maximum element in an array that strictly 
increases to a peak and then strictly decreases, where 0<i<text{length}-1\)'''
#----------------linear search---------------------
def peak(arr):
    n=len(arr)
    ans=0
    for i in range(n):
        if(arr[ans]<=arr[i]):
            ans=i


    return ans        
       

print("peak index linear")
arr = [1,2,3,4,3,2,1]

p = peak(arr)
print(p)

#------------------------binary search-------------
def peak_b(arr):
    n=len(arr)
    ans=0
    low=0
    high=n-1
    for i in range (n):
        mid=(low+high)//2
        if arr[ans]<=arr[mid]:
            ans=mid
        if arr[ans]>arr[mid]:
            low=mid+1
        else:
            high=high-1   

    return ans


print("peak index binary")
arr = [1,2,3,4,3,2,1]
arr=[4,3,2,1]
arr=[1,2,3,4]
p = peak_b(arr)
print(p)                