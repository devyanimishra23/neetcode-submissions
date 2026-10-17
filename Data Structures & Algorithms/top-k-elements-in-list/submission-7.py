class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for num in nums:
            counts[num]=counts.get(num,0)+1
        
        pairs=[]
        for num,count in counts.items():
            pairs.append([count,num])
        pairs.sort()

        result=[]
        for _ in range(k):
            pair=pairs.pop()
            result.append(pair[1])
        
        return result