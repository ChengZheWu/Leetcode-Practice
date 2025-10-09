# https://leetcode.com/problems/time-based-key-value-store/description/
'''
1. Binary Search

m is the size of key, n is the size of value
T: set O(1), get O(logn)
S: O(m*n)
'''
class TimeMap:

    def __init__(self):
        self.map = {} # key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res