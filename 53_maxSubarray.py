"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for i in nums[1:]:
            current_subarray = max(i,current_subarray + i)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray