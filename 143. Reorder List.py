# https://leetcode.com/problems/reorder-list/description/
'''
1. Linked List

T: O(n)
S: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        cur = head
        while prev:
            temp1 = cur.next
            temp2 = prev.next
            cur.next = prev
            prev.next = temp1
            cur = temp1
            prev = temp2