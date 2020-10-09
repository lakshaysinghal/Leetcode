# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self.dfsUtil(root,None,0)
    
    def dfsUtil(self,current,parent,length):
        if not current:
            return length
        if parent and current.val == parent.val+1:
            length+=1
        else:
            length = 1
        return max(length,self.dfsUtil(current.left,current,length),self.dfsUtil(current.right,current,length))
        
        