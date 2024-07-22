/*
 * Here, we keep 2 pointers on 2 sides.
 * Now, we measure the water that can be trapped between these 2 pointers.
 * This is equal to : minimum of the 2 heights * distance between the 2 pointers.
 * 
 * However, there are heights in between as well. We'll have to subtract the heights of the towers in between.
 * 
 * So, we move on to move the pointer to the next higher elevation.
 * On the way, we keep subtracting the height of the towers from the total water trapped.
 *     - If the height of the tower is greater than the max height we've seen so far, we subtract the max height from the total water trapped.
 *     - If the height of the tower is less than the max height we've seen so far, we subtract the height of the tower from the total water trapped.
 */
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length-1, max = 0, total = 0, pmax = 0;
        while(left < right-1) { // repeat until the pointers are 1 apart, because then we can't trap any water.

            // move the left pointer to the next higher elevation
            while(height[left]<=max && left<right-1) {
                left++;

                // subtract the height of the tower from the total water trapped
                if(height[left] >= max) {
                    total -= max;
                } else {
                    total -= height[left];
                }
            }

            // move the right pointer to the next higher elevation
            while(height[right]<=max && left<right-1) {
                right--;

                // subtract the height of the tower from the total water trapped
                if(height[right] >= max) {
                    total -= max;
                } else {
                    total -= height[right];
                }
            }
            
            // the global max height is the minimum of the 2 heights
            // in the next iteration, the pointer that is below the max height will move. so the lower pointer will move.
            pmax = max;
            max = Math.min(height[left], height[right]);

            // add the water trapped between the 2 pointers.
            // we subtract the previous max height because we do not need to re-calculate the overlapping region.
            total += (right-left-1) * (max-pmax);
        }
        return total;
    }
}