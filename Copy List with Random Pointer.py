#Copy List with Random Pointer

#A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

#Return a deep copy of the list.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.nlist={None:None}  #old_node:new_node

        def helper(node):
            if node in self.nlist:
                return self.nlist[node]
            new_node=Node(node.val)
            self.nlist[node]=new_node
            new_node.next=helper(node.next)
            new_node.random=helper(node.random)
            return new_node

        return helper(head)
