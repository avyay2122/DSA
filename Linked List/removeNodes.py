# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        dum = headNew = ListNode(None,head)
        curr = head
        while(curr):
            while(stack and stack[-1].val < curr.val):
                stack.pop()
            stack.append(curr)
            curr = curr.next
        
        for node in stack:
            headNew.next = node
            headNew = headNew.next
        return dum.next
