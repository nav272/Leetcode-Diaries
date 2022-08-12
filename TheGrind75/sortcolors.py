class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        for i in nums:
            if i == 0:
                zeros +=1
            elif i == 1:
                ones +=1
        nums[:zeros] = [0]*zeros
        nums[zeros: zeros+ones] = [1]*(ones)
        nums[zeros+ones:len(nums)] = [2]*(len(nums)-zeros-ones)
        return nums


nums = [1,0,0,0,2,2,2,1,1,1,1,0,2,2,1,1,1]
print(Solution().sortColors(nums))