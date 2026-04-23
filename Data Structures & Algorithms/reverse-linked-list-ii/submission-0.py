# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head
        # reach left
        for i in range(left-1):
            leftPrev, curr = curr, curr.next

        # reverse from l to r
        prev =None
        for i in range(right-left+1):
            tmpNext = curr.next
            curr.next = prev
            prev, curr = curr, tmpNext
        # update pointers
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next