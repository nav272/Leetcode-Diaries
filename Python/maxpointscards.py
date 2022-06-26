
class Solution:
    def maxScore(self, cardPoints, k):
        # cardPoints = [1, 2, 3, 4, 5, 6, 1]
        # k = 3 
        Pointer1 = k -1 
        Pointer2 = len(cardPoints) -1 
        sumofk = sum(cardPoints[:k])
        maximum = sumofk
        for i in range(k):
            sumofk += cardPoints[Pointer2] - cardPoints[Pointer1]
            maximum = max(maximum, sumofk)
            Pointer1 -=1
            Pointer2 -=1
        return maximum

print(Solution().maxScore([1,2,3,4,5,6,1], 3))
