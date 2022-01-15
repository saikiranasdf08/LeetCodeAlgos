'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''


class Solution(object):
    def maxSubArray(self, nums):
        res=float('-inf')
        sum=0
        for i in nums:
            if sum<0 :
                sum=0
            sum = i+ sum
            res=max(res,sum)
        return res
