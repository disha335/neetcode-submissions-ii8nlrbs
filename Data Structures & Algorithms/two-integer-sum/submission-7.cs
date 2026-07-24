public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int n = nums.Length;
        // for(int i=0;i<n-1;i++){
        //     for(int j=i+1;j<n;j++){
        //         if(nums[i]+nums[j]==target)
        //             return [i, j];
        //     }
        // }
        // return [];
        Dictionary<int, int> hMap = new Dictionary<int, int>();
        for(int i=0;i<n;i++){
            int diff = target-nums[i];
            if(hMap.ContainsKey(nums[i])){
                return [hMap[nums[i]], i];
            }
            hMap[diff]=i;
        }
        return [];
    }
}
