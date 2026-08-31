class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        i = 0
        j = 0
        res = []
        nums1.sort()
        nums2.sort()
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1)
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
                
        return res 