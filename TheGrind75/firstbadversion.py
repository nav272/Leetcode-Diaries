class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while(left < right):
            mid = left + int((right-left)/2)
            if Solution.isbadversion(mid):
                right = mid 
            else: 
                left = mid + 1
        return left

    def isbadversion(num):
        if num >= 4:
            return True
        else:
            return False

print(Solution().firstBadVersion(2**31))
