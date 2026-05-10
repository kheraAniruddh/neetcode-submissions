class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t={}    
        substr = [-1,-1]
        for ch in t:
            count_t[ch] = count_t.get(ch, 0)+1
        res = float("infinity")
        for i in range(len(s)):
            countS={}
            for j in range(i, len(s)):
                countS[s[j]] = countS.get(s[j],0)+1
                flag=True
                for ch in count_t:
                    if count_t[ch]>countS.get(ch,0):
                        flag=False
                        break
                if flag and res > j-i+1:
                    res = j-i+1
                    substr =[j,i]                    
        return "" if res== float("infinity") else s[substr[1]:substr[0]+1]


        
            

        