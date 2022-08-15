class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = {}
        max_length = 0
        odd_count = 0
        #count the number of each alphabet in the string
        for i, v in enumerate(s):
            hashset[v] = 1 + hashset.get(v, 0)
        for value in hashset.values():
            if value%2 == 0:
                max_length += value
            else:
                max_length += value - 1
                odd_count = 1
        return max_length + odd_count
