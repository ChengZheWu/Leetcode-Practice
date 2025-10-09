# https://leetcode.com/problems/search-a-2d-matrix/description/
'''
1. Binary Search

T: O(logm + logn)
S: O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid1 = l + (r - l) // 2
            if target < matrix[mid1][0]:
                r = mid1 - 1
            elif target > matrix[mid1][-1]:
                l = mid1 + 1
            else:
                break
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid2 = l + (r - l) // 2
            if target < matrix[mid1][mid2]:
                r = mid2 - 1
            elif target > matrix[mid1][mid2]:
                l = mid2 + 1
            else:
                return True
        return False