'''
15. 3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
Notice that the solution set must not contain duplicate triplets.
'''


def threeSum( nums):
    res=set()
    p,n,z=[],[],0
    Ps,Ns=set(),set()
    for num in nums:
        if num>0:
            p.append(num)
            Ps.add(num)
        elif num<0:
            n.append(num)
            Ns.add(num)
        else:
            z+=1

    if z>0:
        for pn in Ps:
            if -pn in Ns :
                res.add((-pn,0,pn))
    if z>=3:
        res.add((0,0,0))
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            if -(p[i]+p[j]) in Ns:
                res.add((min(p[i],p[j]),max(p[i],p[j]),-(p[i]+p[j])))

    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            if -(n[i]+n[j]) in Ps:
                res.add((min(n[i],n[j]),max(n[i],n[j]),-(n[i]+n[j])))

    return list(res)

print(threeSum([3,0,-2,-1,1,2]))

