# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second portion
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nextS = second.next
            second.next = prev
            prev = second
            second = nextS
        # merge two portions
        first, sec = head, prev
        while sec:
            tmp1, tmp2 = first.next, sec.next
            first.next = sec
            sec.next = tmp1
            first, sec = tmp1, tmp2
