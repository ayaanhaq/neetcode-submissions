# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot)) or self.isSubtree(root.right, subRoot)

        
    def sameTree(self,curr1, curr2):
        if not curr1 and not curr2:
            return True
        if not curr1 or not curr2:
            return False
        if curr1 and curr2 and curr1.val==curr2.val:
            return self.sameTree(curr1.left,curr2.left) and self.sameTree(curr1.right, curr2.right)
        return False