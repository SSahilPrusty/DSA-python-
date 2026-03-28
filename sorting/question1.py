"""Given an array where all elements are sorted in increasing order except two swapped elements, sort it in linear time (no duplicates).
Input:
[3, 8, 6, 7, 5, 9, 10]
Output:
[3, 5, 6, 7, 8, 9, 10]"""


def question(arr):
    i = j = -1

    for k in range(0,len(arr) - 1):
        if arr[k] > arr[k + 1]:
            if i == -1:
                i = k  
                      # first wrong element
            j = k + 1        # second wrong element

    arr[i], arr[j] = arr[j], arr[i]



arr= [3, 8, 6, 7, 5, 9, 10]
question(arr)
print(arr)   