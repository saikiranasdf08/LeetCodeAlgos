'''
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1:ListNode, list2:ListNode):
    res= ListNode(0)
    temp=res
    while list1 and list2:
        if list1.val <list2.val :
            temp.next,list1=list1,list1.next
        else:
            temp.next,list2=list2,list2.next
        temp=temp.next
    temp.next= list1 or list2
    return res.next