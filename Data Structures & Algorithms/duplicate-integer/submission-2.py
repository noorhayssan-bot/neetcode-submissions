class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for e in nums:
            if e in hashset:
                return True
            hashset.add(e)      
        return False     
             
        