/*
 * The solution is based on the fact that the elements of the array are in the range 1 to n.
 * So, we can try to put the element at its correct position.
 * 
 * If the element is already at its correct position, we move to the next element.
 * If the element is not at its correct position, we swap the element with the element at its correct position.
 * 
 * In an attempt to put the element at its correct position, if we find that the element at the correct position is same as the current element, we return the element.
 * That means the element is duplicate.
 * 
 * For example:
 * 
 * nums = [1,3,4,2,2]
 * 
 * We start from the beginning and try to put the element at its correct position.
 * 
 * 1 is at its correct position.
 * 3 is not at its correct position. So, we swap 3 with 4.
 * nums = [1,4,3,2,2]
 * 
 * 4 is not at its correct position. So, we swap 4 with 2.
 * nums = [1,2,3,4,2]
 * 
 * 2 is at the correct position. So we move to the next element.
 * 3 is at its correct position. So we move to the next element.
 * 4 is at its correct position. So we move to the next element.
 * 
 * Now, we have another 2. We check at 2th position and find that the element 2 is already present there.
 * So, 2 is duplicate.
 */

class Solution {
    public int findDuplicate(int[] nums) {
        int element, buff;
        int n = nums.length;
        int i = 0;
        while (i < n) {
            element = nums[i];
            if (i == element - 1) {
                i++;
                continue;
            }

            if (nums[element - 1] == element) {
                return element;
            }

            buff = nums[element - 1];
            nums[element - 1] = element;
            nums[i] = buff;
            if (nums[i] == i + 1) {
                i++;
            }
        }

        return -1;
    }
}

/**
 * Here, we use the slow fast pointer linked list approach.
 * 
 * Let us assume that every element in the array is a node in the linked list.
 * The value of the node is the index of the next node.
 * 
 * For example:
 * 
 * nums = [1,3,4,2,2]
 * 
 * The linked list is:
 * 0 -> 1 -> 3 -> 2 -> 4 -> 2 (loop)
 * 
 * 
 * So first, we use the slow and fast pointer to find the intersection point.
 * Then, we move the slow pointer to the start of the array.
 * We move the slow and fast pointer one step at a time.
 * The point where they meet is the duplicate element.
 * 
 * Refer here for explanation : https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
 */
class Solution2 {
    public int findDuplicate(int[] nums) {
        int slow = nums[0];
        int fast = nums[0];

        do {
            slow = nums[slow];
            fast = nums[fast];
            fast = nums[fast];
        } while(slow !=fast);

        slow = nums[0];
        while(slow != fast){
            slow = nums[slow];
            if (slow == fast) {
                break;
            }
            fast = nums[fast];
        }
        return slow;
    }
}