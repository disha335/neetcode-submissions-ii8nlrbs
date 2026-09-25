# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=deque()
        q.append(root)
        flag=True

        while q:
            n=len(q)
            row=[0]*n
            for i in range(n):
                node=q.popleft()
                ind=i if flag else n-1-i
                row[ind]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #after traversal
            flag=not flag
            res.append(row)
        return res