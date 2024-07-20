/*
 * Convert to set for easy lookup.
 * 
 * Check if the number is the start of a sequence. That can be verified by checking if the number-1 is present in the set.
 * If it is start, look for the end of the sequence by checking if number+1 is present in the set.
 */
class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> st = new HashSet<Integer>();
        for(int i : nums) {
            st.add(i);
        }

        int v, mx=0;
        for(int i : st) {
            v = i;
            if(st.contains(v-1)) {
                continue;
            } else {
                while(st.contains(v+1)) {
                    v++;
                }
                mx = Math.max(mx, v-i+1);
            }
        }

        return mx;
    }
}