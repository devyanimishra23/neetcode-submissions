class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                          

        for j, num in enumerate(nums):    
            complement = target - num      
            if complement in seen:        
                return [seen[complement], j]   
            seen[num] = j   
                

