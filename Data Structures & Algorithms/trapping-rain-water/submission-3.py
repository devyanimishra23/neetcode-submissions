class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_max=[0]*n
        right_max=[0]*n
        best=0
        for i in range(n):
            best=max(best,height[i])
            left_max[i]=best
        
        best=0
        for i in range(n-1,-1,-1):
            best=max(best,height[i])
            right_max[i]=best

        water=0
        for i in range(n):
            water+=min(left_max[i],right_max[i])-height[i]

        return water