class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key=lambda i: i.start)
        
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            l2 = intervals[1]
            
            if i1.end > l2.start:
                return False
        return True
    
    
    