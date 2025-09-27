# https://leetcode.com/problems/encode-and-decode-strings/description/
'''
1. Chunked Transfer Encoding

Calculate the length of each string in list and add the length and a delemiter in front of each string for decoding.

n is the size of list. m is the size of each string in list.
T: O(n*m)
S: O(n*m)
'''
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs: # T: O(n)
            res += str(len(s)) + "#" + s # T: O(m), string += do copy that take S: O(m), use .join will be better.
        return res
    
# more efficient!!!
# class Codec:
#     def encode(self, strs: List[str]) -> str:
#         """Encodes a list of strings to a single string."""
#         res = ""
#         encoded_parts = []
#         for s in strs:
#             encoded_parts.append(str(len(s)) + "#" + s)
#         return res.join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s): # T: O(n)
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length]) # T: O(m), slice do copy that takes S: O(m)
            i = j + 1 + length
        return res