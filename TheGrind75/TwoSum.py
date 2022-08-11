class Solution:
    def twoSum(nums, target):
        seen = {}
        for i, b in enumerate(nums):
            # a + b = target -> a = target - b
            a = target - b
            if a in seen:
                return [seen[a], i]
            seen[b] = i

vegetabletags = [2, 7, 11, 15, 108]
desiredDish = 9
print("I found the ingredients and they can be found at:", Solution.twoSum(vegetabletags, desiredDish))