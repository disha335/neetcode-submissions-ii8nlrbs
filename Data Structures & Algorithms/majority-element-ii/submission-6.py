class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res1, res2 = 0, 0
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == res1:
                cnt1+=1
            elif num == res2:
                cnt2+=1
            elif cnt1==0:
                res1=num
                cnt1=1
            elif cnt2==0:
                res2=num
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1

        cnt1, cnt2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == res1:
                cnt1+=1
            elif nums[i]==res2:
                cnt2+=1
        
        ans = []
        n = len(nums)
        if cnt1>n//3:
            ans.append(res1)
        if cnt2>n//3:
            ans.append(res2)
        return ans
