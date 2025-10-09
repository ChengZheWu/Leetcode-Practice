# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
'''
1. Binary Search

T: O(logn)
S: O(1)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        if nums[0] <= nums[-1]: return res
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
            res = min(res, nums[mid])
        return res