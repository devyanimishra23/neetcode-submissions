class Solution:
    def reorderList(self, head):
        slow=head 
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None
        prev=None
        curr=second
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        second=prev

        first=head
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2

