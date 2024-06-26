# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        dum.next = head
        cur = dum

        while(cur.next):
            prev = cur
            if(cur.next.val == 0):
                cur = cur.next
            if(cur.next):
                cur.val += cur.next.val
                cur.next = cur.next.next
        prev.next = None
        return head