# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float("-inf")
        def dfs(root):
            if not root:
                return 0
            leftSum=max(0,dfs(root.left))
            rightSum=max(0,dfs(root.right))
            self.maxi=max(self.maxi,root.val+leftSum+rightSum)
            return root.val+max(leftSum,rightSum)
        dfs(root)
        return self.maxi