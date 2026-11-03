class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        
        while left<=right:
            mid=(left+right)//2
            row,col=mid//n,mid%n
            value=matrix[row][col]
            if value==target:
                return True
            elif value>target:
                right=mid-1
            else:
                left=mid+1
        return False
