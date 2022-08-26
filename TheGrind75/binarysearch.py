class Solution:
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) -1 
        count = 0
        while(start <= end):
            mid = int(start + (end-start)/2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
            count +=1
            print(count, mid) 
        return -1

print(Solution().binarySearch([i for i in range(10001)], 10000))