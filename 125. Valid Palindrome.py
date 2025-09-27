# https://leetcode.com/problems/valid-palindrome/description/
'''
1. Two Pointers

T: O(n)
S: O(1)
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
'''
1. Two Pointers (without built-in function)

T: O(n)
S: O(1)
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.is_alnum(s[l]):
                l += 1
            while l < r and not self.is_alnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def is_alnum(self, c):
        return ((ord('A') <= ord[c] <= ord['Z']) or
                (ord('a') <= ord[c] <= ord['z']) or
                (ord('0') <= ord[c] <= ord['9']))