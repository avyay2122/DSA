# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        pos = -1
        stack,ans = [],[]
        while(head):
            pos += 1
            ans.append(0)
            while(stack and stack[-1][1]<head.val):
                index,value = stack.pop()
                ans[index] = head.val
            stack.append((pos,head.val))
            head = head.next
        return ans