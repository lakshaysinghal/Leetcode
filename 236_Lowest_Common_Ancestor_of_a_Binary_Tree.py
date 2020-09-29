# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return root
        
        path1 = self.dfs(root,p)
        path2 = self.dfs(root,q)
        i=0
        while(i<len(path1) and i<len(path2) and path1[i]==path2[i]):
            i+=1
        return path1[i-1]
    def dfs(self,root,destination):
        pathStack = []
        if self.dfsUtil(root,destination,pathStack):
            return pathStack
        return []
        
        
    def dfsUtil(self,source,destination,pathStack):
        pathStack.append(source)
        if source == destination:
            return True
        if source.left != None:
            if self.dfsUtil(source.left,destination,pathStack):
                return True
        if source.right != None:
            if self.dfsUtil(source.right,destination,pathStack):
                return True
        pathStack.pop(-1)
        return False