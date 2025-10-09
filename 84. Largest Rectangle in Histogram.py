# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
'''
1. Stack

Monotonic Increasing Stack

T: O(n)
S: O(n)
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, width * height)
            stack.append(i)
        return max_area