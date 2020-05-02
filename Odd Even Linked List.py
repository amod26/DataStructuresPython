#Odd Even Linked List

#Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        elif not head.next:
            return head

        head_odd = head
        head_even = head.next

        node_odd = head
        node_even = head_even

        while node_even.next:
            node_odd.next = node_even.next
            node_odd = node_odd.next

            if node_odd.next:
                node_even.next = node_odd.next
                node_even = node_even.next
            else:
                node_even.next = None

        node_odd.next = head_even

        return head_odd












