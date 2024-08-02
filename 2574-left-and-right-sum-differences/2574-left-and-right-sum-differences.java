class Solution {
    public int[] leftRightDifference(int[] nums) {
        int len=nums.length;
        int[] ans=new int[len];
        for(int i=0;i<len;i++){
            int leftsum=0;
            int rightsum=0;
            for(int j=0;j<i;j++){
                leftsum+=nums[j];
            }
            for(int k=i+1;k<len;k++){
                rightsum+=nums[k];
            }
            if (leftsum>rightsum) {
                ans[i]=leftsum-rightsum;
            }else{
                ans[i]=rightsum-leftsum;
            }
        }
        return ans;
    }
}