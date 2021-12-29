'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printNodes(node):
    h=node
    while h:
        print(h.val,end =" ,")
        h=h.next
head=ListNode(1)
test=head

for i in range(2,6,1):
    test.next=ListNode(i)
    test=test.next

printNodes(head)

def reverseList( head):
    # temp = None
    pre =None
    while head:
        # temp=head.next
        # head.next=pre
        # pre=head
        # head=temp
        head.next,head,pre=pre,head.next,head
    return pre
print("ddd")
printNodes(reverseList(head))