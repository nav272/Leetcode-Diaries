alphanumeric = {'Q', '2', 'P', 'Z', 'v', 'l', '8', 'A', 'Y', 'r', 'O', 'w', 'S', 's', 'm', 'h', 'W', 'e', 'j', 'a', 'u', 'q', 'N', 'D', 'n', 'G', 'b', 'I', 'f', 'L', '1', 'i', 'g', 'd', 'c', 'B', 'J', '5', '0', 't', 'F', 'M', 'k', 'C', 'R', '6', '3', 'K', 'p', 'U', 'V', 'x', 'y', 'z', '7', '4', 'T', 'H', 'X', '9', 'o', 'E'}

class Solution:
    def isPalindrome(self, s):
        s = s.strip()
        left = 0
        right = len(s) - 1
        while left <= right:
            while not Solution.isAlphanumeric(s[left]) and left < right: left +=1
            while not Solution.isAlphanumeric(s[right]) and left < right: right -=1
            if s[left] == s[right] or s[left].upper()==s[right].upper():
                left +=1
                right -=1
            else:
                return False
        return True
        
    def isAlphanumeric(char):
        if char in alphanumeric:
            return True
        else:
            return False
print(Solution().isPalindrome("Harry and Hermione are best friends."))
