# https://leetcode.com/problems/contains-duplicate/description/
'''
1: Brute Force

Use a for loop to check each element for duplicates.

T: O(n^2)
S: O(1)
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    
'''
2. Sorting

For example, given [1, 3, 2, 1], after sorting the array it becomes [1, 1, 2, 3], which makes it easier to check for duplicates.

T: O(nlogn)
S: O(1)
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
    
'''
3. Set

Using a set sacrifices space complexity as a trade-off to achieve improved time complexity.

T: O(n)
S: O(1)
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)