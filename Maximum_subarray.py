class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSub = 0
        
        for n in nums:
            if currSub < 0:
                currSub = 0
                
            currSub += n
            maxSub = max(maxSub, currSub)
            
        return maxSub
    
    