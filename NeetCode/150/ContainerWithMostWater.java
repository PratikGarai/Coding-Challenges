/*
 * We consider the first and the last towers first.
 * 
 * From here on, if we move left or right, the width will decrease and the only way to increase the area is to increase the height.
 * So, whichever tower is smaller, we move that pointer.
 */
class Solution {
    public int maxArea(int[] h) {
        int l=0, r=h.length-1, mx=0;
        while(l<r) {
            mx = Math.max(mx, Math.min(h[l], h[r])*(r-l));
            if(h[l]<h[r]) {
                l++;
            } else {
                r--;
            }
        }
        return mx;
    }
}