/*
Aim is to send 0s to the front and 2s to the back of the array. 1s will adjust themselves automatically.
Have 2 pointers : Left and Right

Left is where 0s will go. Everything less than left are 0s.
Right is where 2s will go. Everything greater than right are 2s.

Iterate through the array.

# Equality Cases (In case idx is at a boundary)
1. If idx == left == 0, move ahead both.
2. If idx == right == 2, the time to break the process. Everything beyond this are sorted 2s.

# Adjustment Cases (adjust left and right in case they are already at pre-placed 0s and 2s)
1. If left == 0, increase left.
2. If right == 2, increase right.

# Switcher Cases
1. If idx == 0 and left != 0, then switch them. Increment left and idx.
2. If idx == 2 and right != 2, the switch thme. Increment idx and decrement right.
*/

class Solution {
    public void sortColors(int[] nums) {
        short left = 0;
        final int len = nums.length;
        short right  = (short)(len-1);
        int buff;
        short idx = 0;

        while(idx<nums.length) {
            if(nums[idx]==0) {
                if(idx==left) {
                    left++;
                    idx++;
                } else if(nums[left]==0) {
                    left++;
                } else {
                    buff = nums[idx];
                    nums[idx] = nums[left];
                    nums[left] = buff;
                    left++;
                }
            }
            else if(nums[idx]==2) {
                if(idx>=right) {
                    break;
                } else if(nums[right]==2) {
                    right--;
                } else {
                    buff = nums[idx];
                    nums[idx] = nums[right];
                    nums[right] = buff;
                    right--;
                }
            }
            else {
                idx++;
            }
        }
    }
}