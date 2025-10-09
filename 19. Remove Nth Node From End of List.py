# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        remove_idx = length - n
        if remove_idx == 0:
            return head.next

        cur = head
        for i in range(remove_idx - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head