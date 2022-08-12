class Solution:
    def merge(self, intervals):
        intervals.sort()
        ans = [intervals[0]]
        for i in intervals:
            if i[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans.append(i)
            print(ans)
        return ans

Solution().merge([[1,3],[2,6],[8,10],[15,18]])