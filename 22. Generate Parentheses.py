# https://leetcode.com/problems/generate-parentheses/description/
'''
1. Backtracking + Stack

T: O( (4^n) / (n * sqrt(n)) )
S: O(n)
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(opened_n, closed_n):
            if opened_n == closed_n == n:
                res.append("".join(stack))
                return
            if opened_n < n:
                stack.append("(")
                backtrack(opened_n + 1, closed_n)
                stack.pop()
            if closed_n < opened_n:
                stack.append(")")
                backtrack(opened_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res