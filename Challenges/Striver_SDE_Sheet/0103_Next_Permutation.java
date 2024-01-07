/*
* If array is in descending order, reverse it.
* Else, search from back till where it is descending. Example : 6, 3, 5, 4, 2, 1
* Here, it is descending till 5. 
* Now, search in the range (5, 4, 2, 1) for a replacement of 3. Here, 4 is valid because 5,3,2,1 also descending.
* Then reverse the range 5,3,2,1
*/

class Solution {
    public void reverse(int[] nums, int beg, int end) {
        int l = end-beg;
        int buff;
        for(int i=0; i<l/2; i++) {
            buff = nums[beg+i];
            nums[beg+i] = nums[end-1-i];
            nums[end-1-i] = buff;
        }
    }

    public void nextPermutation(int[] nums) {
        int len = nums.length;

        int back = len-1;
        while(back>0) {
            if(nums[back]<=nums[back-1]) {
                back--;
            } else {
                break;
            }
        }

        if(back==0) {
            this.reverse(nums, 0, len);
            return;
        }

        int pivot = back-1;
        int replacement = back;

        for(int i=back; i<len; i++) {
            if(nums[i]>nums[pivot]) {
                replacement = i;
            } else {
                break;
            }
        }

        int buff = nums[pivot];
        nums[pivot] = nums[replacement];
        nums[replacement] = buff;

        this.reverse(nums, back, len);
    }
}