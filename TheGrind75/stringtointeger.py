class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if len(s)== 0:
            return 0
        
        sign = 1 
        if s[0] == '-': sign = -1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        number = 0
        for chara in s:
            if chara in "0123456789":
                number = number*10 + int(chara)
            else:
                break
        number = sign * number
        if number >= 2**31:
            return 2**31 -1
        elif number <= -2**31:
            return -2**31 
        return number

print(Solution().myAtoi("words and 987"))
