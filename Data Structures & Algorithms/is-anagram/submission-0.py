class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1={}
        for ch in s:
            if ch in str1:
                str1[ch]+=1
            else:
                str1[ch] = 1    

        for ch in t:
            if ch not in str1:
                return False
            else:
                str1[ch]-=1

        for ch in str1:
            if str1[ch] !=0:
                return False
        return True        



        