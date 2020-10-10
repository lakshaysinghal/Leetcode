# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if (not root1 and root2) or (root1 and not root2):
            return False
        if not root1 and not root2:
            return True
        if root1.val == root2.val:
            return (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)) or (self.flipEquiv(root1.right,root2.left) and self.flipEquiv(root1.left,root2.right))
        return False