# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        wid,remain = divmod(length,k)
        res,cur = [],head
        for i in range(k):
            dum = write = ListNode(0)
            for _ in range(wid + (i<remain)):
                if(cur):
                    write.next = write = ListNode(cur.val)
                    cur = cur.next
            res.append(dum.next)
        return res