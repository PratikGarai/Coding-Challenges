class Solution {
    public int findDuplicate(int[] nums) {
        
        Set<Integer> st = new HashSet<Integer>();
        for(int i=0; i<nums.length; i++) {
            if(st.contains(nums[i])) {
                return nums[i];
            }
            st.add(nums[i]);
        }

        return nums[0];
    }
}
