class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps =defaultdict(list)
        for st in strs:
            temp =''.join(sorted(st))
            maps[temp].append(st)
        
        return list(maps.values())