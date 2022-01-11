"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for index, ch in enumerate(s):
            if count[ch] ==1:
                return index
        return -1