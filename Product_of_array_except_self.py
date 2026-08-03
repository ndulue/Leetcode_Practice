class Solution:
    def productExceptionSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        
        prefix = 1
        for i in range(len(nums)):
            nums[i] *= prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums), -1, -1, -1):
            nums[i] *= postfix
            postfix *= nums[i]
            
        return res
    
    