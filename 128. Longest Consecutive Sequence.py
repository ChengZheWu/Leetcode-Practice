# https://leetcode.com/problems/longest-consecutive-sequence/description/
'''
1. set (Best)

Use set to check each character. If num - 1 doesn't exist, it means it can be the first number and count the consecutive element sequence.

T: O(n)
S: O(n)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for n in num_set:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                max_len = max(length, max_len)
        return max_len