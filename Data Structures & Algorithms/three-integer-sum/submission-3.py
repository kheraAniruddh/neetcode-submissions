class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        for i,n in enumerate(nums):
            ind=[]
            if self.twoSum(i+1, -n, ind, nums):
               for ele in ind:
                res.add(tuple([n] + ele))
        return list(res)

    def twoSum(self, pos: int, tgt: int, res: List[List[int]], nums: List[int]) -> bool:
        l=pos
        r=len(nums)-1
        while l<r:
           if nums[l]+nums[r] == tgt:
                res.append([nums[l], nums[r]])
                l+=1
                r-=1
           elif nums[l]+nums[r] < tgt:
                l +=1
           else:
                r-=1

        return False if len(res)==0 else True