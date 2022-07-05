class Solution:
    def longestConsecutive(self, nums):
        #check if the length of the array is 0
        if len(nums) == 0:
            return 0
        #sort the elements and set the counters
        nums.sort()
        counter = 1 
        maxCounter = 1
        #iterate over each element
        for i in range(1, len(nums)):
            #check for duplicates
            if nums[i] != nums[i-1]:
                #check if the difference is 1 and increment the counter.
                if nums[i] - nums[i-1] ==1:
                    counter +=1
                #if it is not 1, counter is reset
                else:
                    counter = 1
                #in each iteration, the maxcounter is updated.
                maxCounter = max(counter, maxCounter)
        return maxCounter

print(Solution().longestConsecutive([1,2,3,4,100,200]))
