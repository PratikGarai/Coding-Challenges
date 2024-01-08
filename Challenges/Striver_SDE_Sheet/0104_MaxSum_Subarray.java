/*
* If all elements are negative, then the sum is the max element among them
* We start the range of the subarray from the first element and keep adding the subsequent elements in the range
* When the net sum of the subarray becomes <= 0, then there is no need to store consider the range
* And we restart the scanning from the next element
*/

class Solution {
    public int maxSubArray(int[] nums) {
        int maxsum = nums[0];
        int sum = 0;
        int len = nums.length;

        for(int i=0; i<len; i++) {
            sum += nums[i];
            maxsum = Math.max(sum, maxsum);
            sum = Math.max(sum, 0);
        }

        return maxsum;
    }
}