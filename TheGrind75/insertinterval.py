class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for index, interval in enumerate(intervals):
			# the new interval and the current interval don't overlap
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the current interval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
                return result+intervals[index:]
            # in case of overlap
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval); 
        return result
