class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for n in nums:
            if n-1 not in num_set:
                curr_streak=1
                while n+curr_streak in num_set:
                    curr_streak+=1
                res = max(curr_streak, res)
        return res            

        