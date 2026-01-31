'''
the algo proceeds by finding the smallest (or thr largest ,depending on the storing order )element in the unsorted sublist , exchanging (swaping)
it with left most element (putting it in sorted odered) and makeing the sublist boundraies one element to the right
'''
def selection_sort(arr):
    #size of the array
    n= len(arr)
    for i in range (n):
        # asuming the element in i is the minimum
        min_index=i
        #finding the smallest element index in the remaing unsorted part
        for j in range(i+1,n):
            if (arr[j]<arr[min_index]):
                min_index=j
        #swap the found min element with the 1ST element
        arr[i],arr[min_index]=arr[min_index],arr[i]   

    return arr

arr=[9,8,7,6,5,4,3,2,1,0]
print("the unsorted array:- ",arr)
selection_sort(arr)
print("the sorted array :-  ",arr)


'''the time complexity is O(n)
    the space complexity is O(1)
    
    AND IT IS A UNSTABLE SORT '''