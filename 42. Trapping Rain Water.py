# https://leetcode.com/problems/trapping-rain-water/description/
'''
1. Two Pointers

T: O(n)
S: O(1)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        area = 0
        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, height[l])
                if max_left - height[l] > 0:
                    area += (max_left - height[l])
            else:
                r -= 1
                max_right = max(max_right, height[r])
                if max_right - height[r] > 0:
                    area += (max_right - height[r])
        return area