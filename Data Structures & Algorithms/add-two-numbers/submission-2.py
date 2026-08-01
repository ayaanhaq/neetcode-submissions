# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
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
        dummy=ListNode()
        curr=dummy
        for i in res:
            curr.next=ListNode(int(i))
            curr=curr.next
        return dummy.next
        '''
        dummy=ListNode()
        curr=dummy
        carry=0
        

        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0

            total=x+y+carry
            carry=total//10

            curr.next=ListNode(total%10)
            curr=curr.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next

            