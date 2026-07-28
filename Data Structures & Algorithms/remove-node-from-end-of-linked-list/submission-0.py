# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        rm=length-n+1
        if rm==1:
            return head.next
        prev=None
        curr=head
        length=1
        while curr:
            if length==rm:
                prev.next=curr.next
                break
            prev=curr
            curr=curr.next
            length+=1
        return head

