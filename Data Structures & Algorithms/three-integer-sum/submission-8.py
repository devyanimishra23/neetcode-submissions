class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()
        result=[]
        for i in range(len(n)):
            if i>0 and  n[i]==n[i-1]:
                continue
            left=i+1
            right=len(n)-1
            while left < right:

                total=n[i]+n[left]+n[right]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    result.append([n[i],n[left],n[right]])
                    left+=1
                    right-=1
                    while left<right and n[left]==n[left-1]:
                        left+=1
        return result


        