class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left
    
    def insert(self, node):
        prev=self.right.prev
        node.prev=prev
        prev.next=node
        node.next=self.right
        self.right.prev=node
    
    def remove(self, node):
        nxt=node.next
        prev=node.prev

        prev.next=nxt
        nxt.prev=prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newnode=Node(key,value)
        self.cache[key]=newnode
        self.insert(newnode)

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
