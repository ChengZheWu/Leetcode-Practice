# https://leetcode.com/problems/daily-temperatures/description/
'''
1. Stack

T: O(n)
S: O(n)
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for r in range(len(temperatures)):
            while stack and temperatures[r] > temperatures[stack[-1]]:
                l = stack.pop()
                res[l] = r - l
            stack.append(r)
        return res