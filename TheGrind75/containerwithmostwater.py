class Solution:
    def containerwithmostwater(heights):
        left = 0 
        right = len(heights) - 1
        maxarea = 0
        while(left < right):
            if (heights[left] > heights[right]):
                maxarea = max(heights[right]*(right-left), maxarea)
                right -=1
            else:
                maxarea = max(heights[left]*(right-left), maxarea)
                left +=1
        return maxarea

print(Solution.containerwithmostwater([10000, 1, 1, 1, 20, 1,1,1,1,1,1,1,1,1,1,1,10,9]))
