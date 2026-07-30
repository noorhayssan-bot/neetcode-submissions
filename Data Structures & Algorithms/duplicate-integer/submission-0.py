class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occMap = {}
        for i in range (len(nums)):
            occMap [nums[i]] = 1 + occMap.get(nums[i],0)
        for c in occMap:
            if occMap[c] > 1 :
                return True
        return False              
             
             
        