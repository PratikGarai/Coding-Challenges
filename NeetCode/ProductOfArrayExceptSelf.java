/*
 * Left and Right product lists
 * ans[i] = product till i-1 from left * product till i+1 from right
 */
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int l = nums.length;
        int left[] = new int[l];
        int right[] = new int[l];
        int pl = 1, pr = 1;
        for(int i=0; i<l; i++) {
            pl = pl*nums[i];
            pr = pr*nums[l-1-i];
            left[i] = pl;
            right[l-1-i] = pr;
        }

        int ans[] = new int[l];
        for(int i=1; i<l-1; i++) {
            ans[i] = left[i-1] * right[i+1];
        }
        ans[0] = right[1];
        ans[l-1] = left[l-2];

        return ans;
    }
}