class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            chArr = [0]*26
            for ch in s:
                chArr[ord(ch)-ord('a')]+=1
            map[tuple(chArr)].append(s)
        return list(map.values())