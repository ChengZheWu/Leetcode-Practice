# https://leetcode.com/problems/product-of-array-except-self/description/

'''
1. Prefix / Postfix

create a list to save prefix and then mutiply the postfix

T: O(n)
S: O(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
