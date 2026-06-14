class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)

        def dfs():
            if len(nums)==len(perm):
                res.append(perm.copy())
                return
            for num in cnt:
                if cnt[num]>0:
                    perm.append(num)
                    cnt[num]-=1
                    dfs()
                    cnt[num]+=1
                    perm.pop()
        dfs()
        return res

            