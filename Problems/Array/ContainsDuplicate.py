'''
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
'''
def containsDuplicate( nums):
    dic={}
    for n in nums :
        if n in dic:
            return True
        dic[n]=True
    return False