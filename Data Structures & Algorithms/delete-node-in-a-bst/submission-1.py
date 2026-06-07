# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        # find element
        if key>root.val:
            root.right = self.deleteNode(root.right, key)
        elif key<root.val:
            root.left = self.deleteNode(root.left, key)
        # found element to be deleted
        else:
            # if right tree not there , return left (connect to parent)
            if not root.right:
                return root.left
            # if left tree not there , return right(connect to parent)
            if not root.left:
                return root.right
            # find min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            # set root to current val
            root.val = cur.val
            # delete right node
            root.right = self.deleteNode(root.right, root.val)
        return root