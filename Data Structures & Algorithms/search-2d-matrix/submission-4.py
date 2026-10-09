class Solution:
    def searchRow(self,arr,n,target):
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==target:
                return True
            if arr[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            if self.searchRow(matrix[i],n,target):
                return True
        return False