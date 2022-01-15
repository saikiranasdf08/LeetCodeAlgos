'''
23. Merge k Sorted Lists

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        head = ListNode(-1)
        curr=head
        heap=[]
        for l in lists:
            if l:
                heapq.heappush(heap,(l.val,l))
        while heap:
            val,l = heapq.heappop(heap)
            if l.next is not None:
                heapq.heappush(heap,(l.next.val,l.next))
            curr.next=l
            curr=curr.next
        return head.next

