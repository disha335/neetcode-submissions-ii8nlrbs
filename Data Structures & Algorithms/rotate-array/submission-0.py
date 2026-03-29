class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        for i in range(k):
            last = nums[n-1]
            for j in range(n-1, 0, -1):
                nums[j]=nums[j-1]
            nums[0]=last