# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # 1. Find middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse second half
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # 3. Merge two halves
        first, second = head, prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2
