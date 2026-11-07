class Solution:
    def findMin(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        best=nums[0]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<=nums[right]:
                right=mid-1
                best=min(best,nums[mid])
            else:
                left=mid+1
        
        return best

