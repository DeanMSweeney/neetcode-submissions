"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        for i in range(len(intervals) - 1):
            start_i, end_i = intervals[i].start, intervals[i].end
            for j in range(i + 1, len(intervals)):
                start_j, end_j = intervals[j].start, intervals[j].end
                
                # check if meeting j falls within meeting i 
                if start_j >= start_i and start_j < end_i: # j start time 
                    return False
                
                if end_j > start_i and end_j < end_i: # j end time 
                    return False

                if start_j == start_i and end_j == end_i:
                    return False
        return True
                




