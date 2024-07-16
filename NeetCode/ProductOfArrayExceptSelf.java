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

/*
 * Here, we create an emptty ans array.
 * 
 * The next element from a side = present cumulative product till there * element at that index. (because the cumulative product should not include the number).
 * 
 * ans[i+1] = lt;
 * Here lt = cumulatie product from 0 to i.
 * 
 * ans[i-1] = ans[i-1] * rt (update with the right side product)
 * Here rt = cumulatie product from l-1 to i.
 */
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int l = nums.length;
        int ans[] = new int[l];

        int lt = 1;
        ans[0] = 1;
        for(int i=0; i<l-1; i++) {
            lt = lt * nums[i];
            ans[i+1] = lt;
        }

        int rt = 1;
        for(int i=l-1; i>0; i--) {
            rt = rt * nums[i];
            ans[i-1] = ans[i-1] * rt;
        }

        return ans;
    }
}