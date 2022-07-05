class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCounter = 0 
        numsset = set(nums)
        for i in numsset:
          #here the set is not sorted. It's like you scanning the entire room and look for candidate number 100. Once you find 100 you look for 101 and keep doing that till you encounter a number which has the difference greater than 1 
            if i-1 not in numsset:
                j = i+1
                while j in numsset:
                    j +=1
                maxCounter = max(maxCounter, j-i)
        return maxCounter
