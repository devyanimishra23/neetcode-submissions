class Solution:
    def reorderList(self, head):
        # STEP 1: find the middle 🐢🐇
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # STEP 2: bookmark, cut, reverse the second half 📝✂️🔄
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        # STEP 3: weave 🤐
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2