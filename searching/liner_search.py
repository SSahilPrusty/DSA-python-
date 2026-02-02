def liner_search(arr,x):
    n= len(arr)
    index=0
    for i in range(n):
        if arr[i]==x:
            index=i
    return index         




arr=[1,2,356,45,6,78,89]
p=liner_search(arr,45)
print(p)