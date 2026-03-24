""" Merge Sort is a sorting technique that divides a list into halves, sorts them recursively, and then merges the sorted halves to produce a fully sorted list.”

 Key Points
Uses recursion
Based on divide and conquer
Time complexity = O(n log n)
Stable sorting algorithm
"""


def merge_sort(arr):
    # Base condition
    if len(arr) > 1:
        mid = len(arr) // 2
        
        # Divide
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)
        
        # Merge sorted halves
        merge(arr, left, right)


def merge(arr, left, right):
    i = j = k = 0

    # Compare elements from left and right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Add remaining elements from left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Add remaining elements from right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# 🔹 Example usage
arr = [5, 3, 8, 2, 1, 4]
merge_sort(arr)
print("Sorted array:", arr)