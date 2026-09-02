class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        
        while start < end:
            midpoint = (start + end)/2
            if isBadVersion(midpoint):
                end = midpoint
            else:
                start = midpoint + 1
                
        return start