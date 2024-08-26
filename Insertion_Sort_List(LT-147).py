# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode(0)
        current = head
        while current:
            next_node = current.next
            prev_node = sorted_list
            while prev_node.next and prev_node.next.val < current.val:
                prev_node = prev_node.next

            current.next =prev_node.next
            prev_node.next = current

            current = next_node

        return sorted_list.next     