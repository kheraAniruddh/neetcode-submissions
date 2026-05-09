class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = dict()
        l=0
        for i,e in enumerate(s):
            if e  in seen:
                l= max(l, seen[e]+1)  
            seen[e] = i
            res = max(res, i-l+1)
        return res    





        