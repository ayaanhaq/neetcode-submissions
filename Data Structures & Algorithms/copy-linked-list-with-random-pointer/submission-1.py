
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        c={}
        curr=head
        while curr:
            c[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            c[curr].next=c.get(curr.next)
            c[curr].random=c.get(curr.random)
            curr=curr.next
        return c[head]