'''
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
by Two pointers
'''

def hasCycle( head):
    p1=head
    p2=head
    while p2 and p2.next:
        p1=p1.next
        p2=p2.next.next
        if p1==p2:
            return True
    return False