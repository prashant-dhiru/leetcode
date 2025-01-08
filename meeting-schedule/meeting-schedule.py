"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def sortStartTime(val):
            return val.start
        
        no_of_intervals = len(intervals)

        intervals.sort(key=sortStartTime)
        for i in range(no_of_intervals - 1):
            if intervals[i].end > intervals[i+1].start: return False
        return True