class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, countS = {},{}
        res, resInd = float("infinity"), []
        for ch in t:
            countT[ch] = countT.get(ch, 0)+1
        l,r=0,0
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0)+1
            flag=True
            for ch in countT:
                if countS.get(ch,0) < countT[ch]:
                    flag=False
                    break
            while flag:
                if (r-l+1)<res:
                    res = r-l+1
                    resInd = [l,r]
                countS[s[l]] -=1
                l+=1
                for ch in countT:
                    if countS.get(ch,0) < countT[ch]:
                        flag=False
                        break    
        return s[resInd[0]:resInd[1]+1] if res != float("infinity") else ""                   


        