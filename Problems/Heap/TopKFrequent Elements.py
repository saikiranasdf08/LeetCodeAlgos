'''
https://leetcode.com/problems/top-k-frequent-elements/
347. Top K Frequent Elements
'''

import heapq
def topKFrequent( nums, k):
    dic={}
    for i in nums:
        dic[i]=  (1+dic[i]) if i in dic else 1
    heap=[]
    print(dic)
    for key,v in dic.items():
        heapq.heappush(heap,(-1*v,key))
    p=[]
    print(heap)
    for i in range(k):
        v,k=heapq.heappop(heap)
        p.append(k)
    return p


print(topKFrequent([1],1))