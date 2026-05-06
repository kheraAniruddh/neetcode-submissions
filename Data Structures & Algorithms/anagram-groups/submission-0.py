class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps ={}
        res=[]
        for st in strs:
            temp =''.join(sorted(st))
            if temp in maps:
                maps[temp].append(st)
            else:
                maps[temp] = [st]
        for k in maps:
            res.append(maps[k])  
        return res              

