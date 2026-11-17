# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        for i in range(k):
            if not node:
                return head
            node = node.next

        # PART 2: flip the first k nodes (your Reverse Linked List, k times)
        prev = None
        current = head
        for i in range(k):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # PART 3: let recursion flip the rest, and hook it on
        head.next = self.reverseKGroup(current, k)
        return prev