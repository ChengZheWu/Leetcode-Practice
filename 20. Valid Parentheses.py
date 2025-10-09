# https://leetcode.com/problems/valid-parentheses/description/
'''
1. Stack

S: O(n)
T: O(1)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in close_open:
                if stack and stack[-1] == close_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False