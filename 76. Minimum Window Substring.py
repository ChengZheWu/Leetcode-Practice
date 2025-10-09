# https://leetcode.com/problems/minimum-window-substring/description/
'''
1. Sliding Window + HashMap

n is the size of s, m is the size of t
T: O(m + n)
S: O(n)
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_map = {}
        for c in t:
            need_map[c] = 1 + need_map.get(c, 0)
        need = len(need_map)
        have = 0
        min_len = float("inf")
        start_index = 0
        l = 0
        for r in range(len(s)):
            if s[r] in need_map:
                need_map[s[r]] -= 1
                if need_map[s[r]] == 0:
                    have += 1
            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start_index = l
                if s[l] in need_map:
                    if need_map[s[l]] == 0:
                        have -= 1
                    need_map[s[l]] += 1
                l += 1
        if min_len == float("inf"):
            return ""
        else:
            return s[start_index:start_index + min_len]