# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res=[]
        # def postOrder(root):
        #     if not root:
        #         return
        #     postOrder(root.left)
        #     postOrder(root.right)
        #     res.append(root.val)
        # postOrder(root)
        # return res
        res=[]
        if not root:
            return res
        st1,st2=[],[]
        st1.append(root)
        while st1:
            node=st1.pop()
            res.append(node.val)
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        while st2:
            st2.append(st1.pop().val)
        return res[::-1]

