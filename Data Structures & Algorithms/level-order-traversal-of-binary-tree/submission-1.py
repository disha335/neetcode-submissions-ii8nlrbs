# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append(root)
        res=[]
        if not root:
            return res
        while q:
            
            n=len(q)
            row=[0]*n
            for i in range(n):
                node=q.popleft()
                row[i]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(row)
        return res
            
