"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        train = ListNode(float('-inf'))
        train.next = head
        pre , curr = train , train.next
        
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre  = curr
            curr = curr.next
        
        return train.next