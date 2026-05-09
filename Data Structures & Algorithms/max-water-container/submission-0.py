class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxo=0
        while l<r:
            cand= (r-l)* min(heights[l], heights[r])
            maxo = max(cand, maxo)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxo            




        