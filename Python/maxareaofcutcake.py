class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        #sort the cuts in increasing order
        horizontalCuts.sort()
        verticalCuts.sort()
        #horizontal and vertical distance
        horizontalDis= 1
        verticalDis = 1
        #vertical and horizontal start and end points
        horizontalStart = horizontalCuts[0]
        horizontalend = h - horizontalCuts[-1]
        verticalstart = verticalCuts[0]
        verticalend = w - verticalCuts[-1]
        #we calculate the maximum distance
        if len(horizontalCuts) == 1:
            horizontalDis = max(horizontalStart, horizontalend)
        if len(verticalCuts) == 1:
            verticalDis = max(verticalstart, verticalend)

        for i in range(1, len(horizontalCuts)):
            horizontalDis = max(horizontalDis, horizontalStart, horizontalend, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            verticalDis = max(verticalDis, verticalstart, verticalend, verticalCuts[i]-verticalCuts[i-1])

        #we return the maxarea%(10**9+7)
        return (horizontalDis*verticalDis)%(10**9+7)
