class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        #a tuple to store the max value of left and right pointer length
        max_length_pointer = (0,0)
        for i in range(n):
            #odd case 
            left = i
            right = i
            while left >=0 and right < n and s[left] == s[right]:
                left -=1
                right +=1
            if (right - left +1) > max_length_pointer[1] - max_length_pointer[0]:
                max_length_pointer = (left, right)
            left =i
            right = i+1
            while left >=0 and right < n and s[left] == s[right]:
                left -=1
                right +=1
            if (right - left +1) > max_length_pointer[1] - max_length_pointer[0]:
                max_length_pointer = (left, right)
        return s[max_length_pointer[0] +1:max_length_pointer[1]]
