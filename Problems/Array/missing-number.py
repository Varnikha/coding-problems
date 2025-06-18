Problem: Missing Number
Platform: LeetCode #268
Difficulty: Easy
Date Solved: 2024-06-18
Time Complexity: O(n)
Space Complexity: O(1)

Problem Description:
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Solution 1:

class Solution(object):
    def missingNumber(self, nums):
        res=len(nums)
        for i in range (len(nums)):
            res+=i
            res-=nums[i]
        return res

Link : 
https://leetcode.com/problems/missing-number/
