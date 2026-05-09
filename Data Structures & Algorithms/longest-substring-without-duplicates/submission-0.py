class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i,e in enumerate(s):
            j=i+1
            seen=set(s[i])
            while j<len(s):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    j+=1 
            res= max(res, j-i)
        return res            


        