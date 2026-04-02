"""🧩 Problem: Majority Element(leet code 169)

Statement:

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

📥 Input
An integer array nums
📤 Output
Return the majority element
🧪 Examples
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2"""


# my solution but time limit exceed 45/63 cases passed
def ma(arr, n):
    for i in range(0, n):
        c = 0
        for j in range(i, n):
            if arr[i] == arr[j]:
                c += 1

        if c > n // 2:
            return arr[i]
        

 #"""MOORE'S VOTING ALGO"""       
#chatgpt soltuion 
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

arr= [2,2,1,1,1,2,2]      
s=ma(arr,7)
print(s)