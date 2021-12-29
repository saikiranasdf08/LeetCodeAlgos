'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists( lists):
    res= ListNode(0)
    temp=res
    while hasNodes(lists):
        minIdx=-1
        minNode=ListNode(float('inf'))
        for i,node in enumerate(lists):
            if node and node.val<minNode.val:
                minNode=node
                minIdx=i
        temp.next=minNode
        lists[minIdx]=minNode.next
        temp=temp.next
        return res.next



def hasNodes(lists):
    for node in lists:
        if node:
            return True
    return False

