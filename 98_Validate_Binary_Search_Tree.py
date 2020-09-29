# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTUtil(root,-(2**32),2**32-1)
    
    def isValidBSTUtil(self,root,lowerLimit,upperLimit):
        if not root:
            return True
        if root.val <= lowerLimit or root.val >= upperLimit:
            return False
        return self.isValidBSTUtil(root.left,lowerLimit,root.val) and self.isValidBSTUtil(root.right,root.val,upperLimit)