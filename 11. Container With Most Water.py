# https://leetcode.com/problems/container-with-most-water/description/
'''
1. Two Pointers

T: O(n)
S: O(1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            h = min(height[l], height[r])
            water = h * (r - l)
            max_water = max(max_water, water)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_water