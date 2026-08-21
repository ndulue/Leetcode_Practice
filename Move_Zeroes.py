class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        i = 0
        for j in range(nums):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
