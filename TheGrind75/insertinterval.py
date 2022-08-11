import random

class Solution:
    def insertIntervals(intervals, newInterval):
        results = []
        startTimePosition = 0
        endTimePosition = 1
        for index, interval in enumerate(intervals):
            #first condition where the current interval's end position is less than newInterval's start position, just add the current interval as is.
            if interval[endTimePosition] < newInterval[startTimePosition]:
                results.append(interval)
            #second condition where the current interval's start is greater than newInterval's end, just add the new interval and return the rest of the intervals list
            elif interval[startTimePosition] > newInterval[endTimePosition]:
                print("2nd one")
                results.append(newInterval)
                return results + intervals[index:]
            #third condition is when there is an overlap, end of current interval is greater than or equal to start of the new Interval or start of the current interval is less than or equal to the end of the new Interval
            else:
                newInterval[startTimePosition] = min(newInterval[startTimePosition], interval[startTimePosition])
                newInterval[endTimePosition] = max(newInterval[endTimePosition], interval[endTimePosition])
        results.append(newInterval)
        return results

print(Solution.insertIntervals([[1,3],[6,9]], [3,7]))
