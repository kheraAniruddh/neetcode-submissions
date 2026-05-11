# if l < r:
#      return l
#  else:
#    l = mid
#       if l-1<l < l+1   
#           r=mid
#       else
#           
# 
# 
# 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        l,r= 0, len(nums)-1
        while l<r:
            mid = l + (r-l)//2
            if nums[mid] <nums[r]:
                r=mid
            else:
                l=mid+1    
        return nums[l]                   


        