class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        count=dict()
        for n in nums:
            count[n] = count.get(n,0)+1
        for n in count.keys():
            heapq.heappush(pq,(count[n],n))
            if len(pq)>k:
                heapq.heappop(pq)
        return list(ele[1] for ele in pq)        
        