class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        
        rooms = 0
        count = 0
        s = 0
        e = 0
        
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            rooms = max(rooms, count)