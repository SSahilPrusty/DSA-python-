"""Cycle Sort Definition:

Cycle Sort is an in-place, comparison-based sorting algorithm that works 
by placing each element in its correct position in the array through cycles of rotations.
It minimizes the number of memory writes by ensuring each element is written only once to its final position.
The algorithm determines the correct position of an element by counting how many elements are smaller than
it and then rotates the cycle until all elements are placed correctly.

Time Complexity: O(n²)
Space Complexity: O(1)
Key Feature: Minimum number of writes (optimal for write-sensitive memory)"""


def cycle_sort(arr):
    n = len(arr)

    for cyclestart in range(n - 1):
        item = arr[cyclestart]
        pos = cyclestart

        # Find correct position
        for i in range(cyclestart + 1, n):
            if arr[i] < item:
                pos += 1

        # If already correct
        if pos == cyclestart:
            continue

        # Skip duplicates
        while item == arr[pos]:
            pos += 1

        # Swap
        arr[pos], item = item, arr[pos]

        # Rotate rest of cycle
        while pos != cyclestart:
            pos = cyclestart

            for i in range(cyclestart + 1, n):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            arr[pos], item = item, arr[pos]

    return arr



arr=[1,7,456,876,35,0]
print("the unsorted array:-",arr)
cycle_sort(arr)
print("the sorted array:-",arr)
