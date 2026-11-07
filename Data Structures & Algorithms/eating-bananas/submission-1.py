import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left=1
        right=max(piles)
        best=right
        while left<=right:
            mid=(left+right)//2

            total=0
            for pile in piles:
                hours=math.ceil(pile/mid)
                total+=hours

            if total<=h:
                best=min(best,mid)
                right=mid-1
            else:
                left=mid+1

        return best 