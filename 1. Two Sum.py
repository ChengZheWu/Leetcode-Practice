#https://leetcode.com/problems/two-sum/description/
'''
1. Brute Force

Check every pair of elements if their sum equals to the target.

T: O(n^2)
S: O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return
    
'''
2. HashMap (Best)

Use a hash table to store element indices, and while iterating check if target - current element exists; if yes, return the solution.

T: O(n)
S: O(n)
''' 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[n] = i
        return 