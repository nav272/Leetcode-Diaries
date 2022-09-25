class Solution:
    def JobScheduling(self, start, end, profit):
        jobs = sorted(zip(start, end, profit))
        start.sort()
        N = len(start)
        maxprofit = [0 for i in range(N)]
        maxprofit[-1] = jobs[-1][2]
        def nextstart(left, right, target):
            if left>right:
                return left
            mid = left + int((right-left)/2)
            if start[mid] >= target:
                return nextstart(left, mid-1, target)
            else:
                return nextstart(mid+1, right, target)
        for i in range(N-2, -1, -1):
            index = nextstart(start[0], start[-1], jobs[i][1])
            profit = maxprofit[index] if index<N else 0
            maxprofit[i] = max(profit + jobs[i][2], maxprofit[i+1])
        return maxprofit[0]
