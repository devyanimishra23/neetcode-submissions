class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[0]*n
        result[0]=1

        for i in range(1,n):
            result[i]=result[i-1]*nums[i-1]

        right_product=1
        for i in range(n-1,-1,-1):
            result[i]=result[i]*right_product
            right_product*=nums[i]
        
        return result

