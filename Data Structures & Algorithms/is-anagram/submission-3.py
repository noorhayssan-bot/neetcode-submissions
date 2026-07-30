class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        strMap_1,strMap_2 = {},{}

        for i in range(len(s)):
            strMap_1[s[i]] = 1 + strMap_1.get(s[i],0)
            strMap_2[t[i]] = 1 + strMap_2.get(t[i],0)
        for c in strMap_1:
            if strMap_1[c] != strMap_2.get(c,0):
                return False

        return True        
           

             





        