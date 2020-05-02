# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None

        prev = None
        p = head

        while p is not None:
            if p.val == val:
                if prev is None:
                    head = p.next
                else:
                    prev.next = p.next
            else:
                prev = p
            p = p.next
        return head

    
    #Adding a sentinel Node
    # Sentinel node is nothing but an empty list which can be initialized at the head or tail of the linkedlist
    
     def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next
