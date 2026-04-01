"""📝 Problem Statement

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
 representing the number of elements in nums1 and nums2 respectively.

👉 Merge nums1 and nums2 into a single array sorted in non-decreasing order.

⚠️ Important Condition
The final sorted array should NOT be returned
Instead, it must be stored inside nums1
nums1 has size m + n
First m elements → valid elements
Last n elements → 0 (empty space)
📥 Examples
Example 1
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Output:
[1,2,2,3,5,6]
Example 2
Input:
nums1 = [1], m = 1
nums2 = [], n = 0

Output:
[1]
Example 3

Input:
nums1 = [0], m = 0
nums2 = [1], n = 1

Output:
[1]"""

def Q(nums1, nums2, m, n):
    i = m - 1
    j = n - 1
    last = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1

    # copy remaining nums2 elements
    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Q(nums1,nums2,m,n)
print(nums1)