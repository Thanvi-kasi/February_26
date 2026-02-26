# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pointerA = headA
        pointerB = headB
        
        # When either pointer hits the end, redirect it to the other head.
        # If the lists intersect, the pointers will meet at the intersection node.
        # If not, both will eventually become None at the same time.
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA
