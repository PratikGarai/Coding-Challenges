/**
 Check using set
 Sapce : O(n)
 Time : O(n)
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> h = new HashSet<Integer>();
        for(int i: nums) {
            if(h.contains(i)) {
                return true;
            } else {
                h.add(i);
            }
        }
        return false;
    }
}