# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        dusra=slow.next
        slow.next=None

        middle=dusra
        prev=None

        while middle:
            nxt=middle.next
            middle.next=prev
            prev=middle
            middle=nxt
        
        p1=head
        p2=prev

        while p2:
            next1=p1.next
            next2=p2.next

            p1.next=p2
            p2.next=next1

            p1=next1
            p2=next2