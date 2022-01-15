'''
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

def findMin( nums) -> int:
    start, end =0,len(nums)-1

    while start<end :
        mid =(end+ start)//2

        if nums[mid] >nums[end]:
            start=mid+1
        else:
            end=mid
    return nums[start]