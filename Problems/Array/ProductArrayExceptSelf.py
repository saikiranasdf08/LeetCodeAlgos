'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
'''
def productExceptSelf( nums):
    k=1
    result=[]
    for i in range(len(nums)):
        result.append(k)
        k=k*nums[i]
    print(result)
    k=1
    for i in range(len(nums)-1,-1,-1):
        result[i] = k * result[i]
        k = k * nums[i]
    return result