public class Solution {
    public void swap(int[]nums, int x, int y){
        int tmp = nums[x];
        nums[x]=nums[y];
        nums[y]=tmp;
    }
    public void SortColors(int[] nums) {
        int l=0;
        int curr=0;
        int r=nums.Length-1;
        while(curr<=r){
            if(nums[curr]==0){
                swap(nums, curr,l);
                l++;
            }
            else if(nums[curr]==2){
                swap(nums, curr, r);
                r--;
                curr--;
            }
        curr+=1;
        }
    }
}