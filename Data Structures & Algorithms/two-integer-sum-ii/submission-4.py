class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        left=0
        right=len(n)-1
        while left<right:
            total=n[left]+n[right]
            if total>target:
                right-=1
            elif total<target:
                left+=1
            else:
                return [left+1,right+1]