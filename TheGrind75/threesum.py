class Solution:
    def threeSum(self, nums):
        nums.sort() #sort the array
        n, result = len(nums), []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue #skip the duplicates
            #logic a +b +c =0, a + b = -c 
            target = -nums[i]
            start, end = i + 1, n - 1

            while start < end:
                if nums[start] + nums[end] < target: #move the start pointer towards right if less than target
                    start += 1
                elif nums[start] + nums[end] > target:#shift the end pointer towards left if greadter than target
                    end -= 1
                else:
                    if len(result) ==0 or result[-1] != (nums[i], nums[start], nums[end]):
                        result.append((nums[i], nums[start], nums[end])) # if a + b = -c, add to results if similar results don't exist
                    start += 1
                    end -= 1

        return result
        
 
 mypairfindingsample = [0,1,2,-1,-2]
 print(Solution.threesum(mypairfindingsample)
