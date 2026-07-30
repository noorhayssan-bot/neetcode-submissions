class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strMap_1 = {}
        strMap_2 = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c in strMap_1:
                strMap_1[c] += 1
            else:
                strMap_1[c] = 1
        for l in t:    
            if l in strMap_2:
                strMap_2[l] += 1
            else:
                strMap_2[l] = 1  
        return  strMap_1 == strMap_2        





        