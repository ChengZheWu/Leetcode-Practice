# https://leetcode.com/problems/koko-eating-bananas/description/
'''
1. Binary Search

p is the size of piles
T: O(p * log(max(p)))
S: O(1)
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            t = 0
            for p in piles:
                t += ceil(p / mid)
            if t > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res