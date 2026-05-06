class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps ={}
        for i, n in enumerate(nums):
            if n in maps:
                return [maps[n], i]
            maps[target-n] = i
        return  [-1,-1]