# https://leetcode.com/problems/valid-anagram/description/
'''
1. HashMap (Best)

Create 2 HashMap to count each element in those 2 lists, and then check them one by one.

n is the size of s, m is the size of t.
T: O(n + m)
S: O(1) Since there are only 26 English characters
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        hashmap_t = {}
        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i], 0)
        return hashmap_s == hashmap_t


'''
2. Sorting

Sort inputs ans compare each element

T: O(nlogn + mlogm)
S: O(1) depend on sorting alogirthm
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)