# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = odd = ListNode(0)
        head2 = even = ListNode(0)
        i = 0
        while(head):
            if(i%2 == 0):
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            head = head.next
            i+=1
        odd.next = None
        even.next = head1.next
        return head2.next