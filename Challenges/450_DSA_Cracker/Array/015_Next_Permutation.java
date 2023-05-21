class Solution {
    public void reverse(int[] nums, int begin, int end) {
        int mid = (end-begin)/2;
        int k;
        for(int i=0; i<mid; i++) {
            k = nums[begin+i];
            nums[begin+i] = nums[end-i-1];
            nums[end-i-1] = k; 
        }
    }

    public void nextPermutation(int[] nums) {
        
        int l = nums.length;
        if(l==1) {
            return;
        }

        int ind = l-2;
        while(ind>=0 && nums[ind]>=nums[ind+1]) {
            ind--;
        }

        if(ind==-1) {
            this.reverse(nums, 0, l);
        } else {
            int ele = nums[ind];
            int tind = ind;
            this.reverse(nums, ind+1, l);
            ind++;
            while(ind<l && nums[ind]<=ele) {
                ind++;
            }
            nums[tind] = nums[ind];
            nums[ind] = ele;
        }
    }
}
