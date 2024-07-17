class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mapper = new HashMap<>();
        int[] res = new int[2];
        for(int i = 0; i<nums.length; i++) {
            if(mapper.containsKey(target-nums[i])) {
                res[0] = i;
                res[1] = mapper.get(target-nums[i]);
                break;
            } else {
                mapper.put(nums[i], i);
            }
        }
        return res;
    }
}