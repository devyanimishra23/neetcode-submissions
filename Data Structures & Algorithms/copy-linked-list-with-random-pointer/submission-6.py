"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_of={None:None}
        
        node=head
        while node:
            new_node=Node(node.val)
            copy_of[node]=new_node
            node=node.next
        
        node=head
        while node:
            my_copy=copy_of[node]
            my_copy.next=copy_of[node.next]
            my_copy.random=copy_of[node.random]
            node=node.next
        
        return copy_of[head]

