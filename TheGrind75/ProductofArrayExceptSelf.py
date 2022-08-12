import random
class Solution:
    def productExceptSelf(nums):
        answer = [1]*len(nums)
        suffix = 1
        prefix = 1
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]
            answer[-1-i] *= suffix
            suffix *= nums[-1-i]
            print("prefix: ", prefix, "suffix: ", suffix, answer)
        return answer

nums = random.sample(range(1, 10), 5)
print(nums)
print(Solution.productExceptSelf(nums))