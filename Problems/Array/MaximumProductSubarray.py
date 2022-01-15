'''
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


'''

class Solution(object):
    def maxProduct(self, nums):
        res=nums[0]
        minprd,maxprd=1,1

        for num in nums:
            tup=(num,num*minprd,num*maxprd)
            minprd,maxprd=min(tup),max(tup)

            res=max(maxprd,res)

        return res
