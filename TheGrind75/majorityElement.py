class Solution(object):
  #method 1: Sorting
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]
  #method 2: hashset
    def majorityElement2(self, nums):
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
            if m[n] > len(nums)//2:
                return n
