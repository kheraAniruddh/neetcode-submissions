class Solution:
#  l=r=0, 
#  if p[r]>p[l] = > max(max, p[r]-p[l]); r++
#  else:
#   l++
# 
# 
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        l,r,res=0,1,0
        while l<len(prices) and r<len(prices):
            if prices[l] <= prices[r]:
                res = max(res, prices[r]-prices[l])
                r+=1
            else:
                l=r 
                r+=1
        return res           

        