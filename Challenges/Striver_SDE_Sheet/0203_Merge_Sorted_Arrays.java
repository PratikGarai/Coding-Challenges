/*
Use 3 pointers, 2 for nums1 and 1 for nums2

The pointers are : 
idx1 = m-1, points to last to be processed element of nums1
idx2 = n-1, points to last to be processed element of nums2
ins = m+n-1, points to last element where insertion is to be done

Now, we start from the end of both arrays and keep comparing the elements at idx1 and idx2.
Whichever is greater, we put it at ins and decrement the respective pointers and ins.


======= Reason to start from the end and not the beginning 
If we start from the beginning, we will have to shift the elements of nums1 to the right to make space for the elements of nums2.
But if we start from the end, we can simply put the elements of nums2 at the end of nums1 without worrying about shifting the elements of nums1.

Example:
nums1 = [4,5,6,0,0,0], m = 3
nums2 = [1,2,3], n = 3

Here, if we start from the beginning, we'll end up with :
nums1 = [1,5,6,0,0,0]
nums2 = [4,2,3]

But 4 should be at the end of nums2 and not at the beginning. So the tatic will not work from the beginning.
*/

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        int idx1=m-1, idx2=n-1, ins=m+n-1;
        while(idx1>=0 && idx2>=0) {
            if(nums1[idx1]>nums2[idx2]) {
                nums1[ins--] = nums1[idx1--];
            } else  {
                nums1[ins--] = nums2[idx2--];
            }
        }

        while(idx2>=0) {
            nums1[ins--] = nums2[idx2--];
        }

        while(idx1>=0) {
            nums1[ins--] = nums1[idx1--];
        }
    }
}