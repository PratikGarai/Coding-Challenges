/*
 * Sort first, that will make it easier to filter out duplicates.
 * 
 * First, choose and anchor, then run twoSum on the rest of the array.
 * 
 * Filtering duplicates : 
 * 1. For the anchor, if the current element is the same as the previous element, skip it.
 * 2. For the twoSum, if the left or right element is the same as the previous element, skip it.
 */
class Solution {
    public static void twoSum(int[] nums, int left, int right, int anchor, List<List<Integer>> res) {
        int target = -1 * anchor, s;
        while(left < right) {
            s = nums[left] + nums[right];
            if(s<target) {
                left++;
            } else if(s>target) {
                right--;
            } else {
                res.add(new ArrayList<Integer>(Arrays.asList(anchor, nums[left++], nums[right--])));
                while(left < right && nums[left]==nums[left-1])
                    left++;
                while(left < right && nums[right]==nums[right+1])
                    right--;
            }
        }
    }

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for(int i=0; i<nums.length-2; i++) {
            if(nums[i] > 0) {
                break;
            }
            if(i>0 && nums[i-1]==nums[i]) {
                continue;
            }
            twoSum(nums, i+1, nums.length-1, nums[i], res);
        }

        return res;
    }
}