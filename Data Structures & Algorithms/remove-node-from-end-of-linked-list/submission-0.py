# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        zero_node = ListNode(0, head)
        l, r = zero_node, head

        while n>0 and r:
            r = r.next
            n-=1
        while r:
            l = l.next
            r = r.next
        
        # delete
        l.next = l.next.next
        return zero_node.next