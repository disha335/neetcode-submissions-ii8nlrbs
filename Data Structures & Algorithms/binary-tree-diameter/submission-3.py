# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findHeight(self,root):
        if not root:
            return 0
        return 1+max(self.findHeight(root.left),self.findHeight(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def dfs(root):
            if not root:
                return
            lH=self.findHeight(root.left)
            rH=self.findHeight(root.right)
            self.maxi=max(self.maxi,lH+rH)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.maxi