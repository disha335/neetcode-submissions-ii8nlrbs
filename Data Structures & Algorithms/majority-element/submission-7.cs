public class Solution {
    public int MajorityElement(int[] nums) {
        // Dictionary <int, int> hMap = new Dictionary <int, int>();
        // int n = nums.Length;
        // foreach(int num in nums){
        //     if(hMap.ContainsKey(num))
        //         hMap[num]++;
        //     else
        //         hMap[num]=1;
        // }
        // foreach(KeyValuePair<int, int> pair in hMap){
        //     if(pair.Value>(n/2))
        //         return pair.Key;
        // }
        // return -1;

        int ele = 0;
        int cnt = 0;
        foreach(int num in nums){
            if(cnt==0)
                ele=num;
            if(ele==num)
                cnt++;
            else
                cnt--;
        }
        return ele;
    }
}