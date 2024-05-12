"""

169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
"""

class Solution(object):
    def majorityElement(self,nums):
        n = len(nums)//2
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num] = 1
        for number , count in dict1.items():
            if count > n:
                return number 

