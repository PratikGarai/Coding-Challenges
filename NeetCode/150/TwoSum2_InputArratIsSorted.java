class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1, s;
        int[] res = new int[2];
        while(left < right) {
            s = numbers[left] + numbers[right];
            if(s < target) {
                left++;
            } else if (s>target) {
                right--;
            } else {
                res[0] = left+1;
                res[1] = right+1;
                break;
            }
        }

        return res;
    }
}