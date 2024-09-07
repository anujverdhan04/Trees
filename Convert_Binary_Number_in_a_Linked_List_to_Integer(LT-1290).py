# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        binary_str = ""
        while head:
            binary_str += str(head.val)
            head = head.next
        return int(binary_str , 2)    



'''        
        if not head:
            return 0
        result = 0
        while head:
            result = (result <<1) | head.val
            head= head.next
        return result    

'''       
        