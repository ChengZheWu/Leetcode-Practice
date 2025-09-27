# https://leetcode.com/problems/top-k-frequent-elements/description/
'''
1. Bucket sort (Best)

T: O(n)
S: O(n)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
'''
2. MinHeap

T: O(klogn)
S: O(n)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        minheap = []
        for num, cnt in count.items():
            heapq.heappush(minheap, (cnt, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
    
'''
3. Sorting

T: O(nlogn)
S: O(n)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        arr = []
        for num, cnt in count.items():
            arr.append((cnt, num))
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res