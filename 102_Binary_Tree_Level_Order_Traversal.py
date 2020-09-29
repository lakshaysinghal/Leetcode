# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root,None]
        result = []
        current_level=[]
        while len(queue)>0:
            current = queue.pop(0)
            if current == None:
                result.append(current_level)
                current_level=[]
                if len(queue) >0:
                    queue.append(None)
            else:
                current_level.append(current.val)
                print(current.val)
                if current.left!=None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
        return result
        