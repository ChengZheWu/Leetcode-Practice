# https://leetcode.com/problems/group-anagrams/description/
'''
1. HashMap (Best)

Use 26 English characters to record each string, and each anagram has the same key. Then we can get the result.

m is the size of list, n is the size of each string in list.
T: O(m*n)
S: O(m*n)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

'''
2. Sorting

Sort each string as its key, then we can get the result.

m is the size of list, n is the size of each string in list.
T: O(m*nlogn)
S: O(m*n)  sorted may use O(n) in each loop, but it will not expand by n.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)
        return list(res.values())