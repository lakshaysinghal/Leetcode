# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        visited = {}
        inorder = []
        while len(stack)>0:
            peek = stack[-1]
            if peek.left and peek not in visited:
                stack.append(peek.left)
                visited[peek]=True
                continue
            inorder.append(peek.val)
            stack.pop(-1)
            visited[peek]=True
            
            if peek.right:
                stack.append(peek.right)
                
        return inorder
            
                
        
        