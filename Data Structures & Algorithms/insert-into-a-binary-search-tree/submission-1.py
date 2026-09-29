# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr=root
        while True:
            if curr.val<=val:
                if curr.right:
                    curr=curr.right
                else:
                    node=TreeNode(val)
                    curr.right=node
                    break
            else:
                if curr.left:
                    curr=curr.left
                else:
                    node=TreeNode(val)
                    curr.left=node
                    break
        return root
            