class Solution:
#  l=r=0, 
#  if p[r]>p[l] = > max(max, p[r]-p[l]); r++
#  else:
#   l=r, r++
# 
# 
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        l,r,res=0,1,0
        while r<len(prices):
            if prices[l] <= prices[r]:
                res = max(res, prices[r]-prices[l]) 
            else:
                l=r 
            r+=1  
        return res           

        