# https://leetcode.com/problems/sliding-window-maximum/description/
'''
1. Sliding Window + Monotonic Decreasing Deque

Let the largest number at the front

T: O(n)
S: O(n)
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # monotonic decreasing dequeu
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop() # pop is from right, popleft is from left
            q.append(r) # add is from left, append is from right

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
        return res