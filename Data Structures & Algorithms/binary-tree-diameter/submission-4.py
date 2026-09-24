# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def dfs(root, maxi):
            if not root:
                return 0
            
            left=dfs(root.left,maxi)
            right=dfs(root.right,maxi)
            self.maxi=max(self.maxi,left+right)
            return 1+max(left,right)
        dfs(root,self.maxi)
        return self.maxi