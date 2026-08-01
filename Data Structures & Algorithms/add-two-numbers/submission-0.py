# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        s1=""
        s2=""
        while curr1:
            s1+=str(curr1.val)
            curr1=curr1.next
        while curr2:
            s2+=str(curr2.val)
            curr2=curr2.next
        res=int(s1[::-1])+int(s2[::-1])
        res=(str(res)[::-1])
        print(res)
        dummy=ListNode()
        curr=dummy
        for i in res:
            curr.next=ListNode(int(i))
            curr=curr.next
        return dummy.next