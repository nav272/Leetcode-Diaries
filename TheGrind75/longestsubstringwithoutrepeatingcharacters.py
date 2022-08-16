class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hashtable = {}
        left, right = 0, 0
        maximum_window = 0
        while right < len(s):
            if s[right] in hashtable and left <= hashtable[s[right]]:
                left = hashtable[s[right]] + 1
            else: 
                maximum_window = max(maximum_window, right -left +1)
            hashtable[s[right]] =right
            right +=1
        return maximum_window