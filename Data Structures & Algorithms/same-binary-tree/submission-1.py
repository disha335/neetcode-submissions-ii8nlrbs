# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # q1 = deque([p])
        # q2 = deque([q])
        # while q1 and q2:
        #     for _ in range(len(q1)):
        #         curr1 = q1.popleft()
        #         curr2 = q2.popleft()
        #         if curr1 is None and curr2 is None:
        #             continue
        #         if curr1 is None or curr2 is None or curr1.val!=curr2.val:
        #             return False
        #         q1.append(curr1.left)
        #         q1.append(curr1.right)
        #         q2.append(curr2.left)
        #         q2.append(curr2.right)
        # return True

        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False