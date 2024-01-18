/*

Take the element at 0,1 of a 4x4 matrix.
Index it on the basis of layer and index. 

0,1 will be in layer 0 and index 1.
Check for replacement logics.

Points to note:
1. There will be alternates of layer and idx usage in the replacement logic.

*/

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int layers = n/2;
        int buff;
        for(int layer=0; layer<layers; layer++) {
            for(int idx=layer; idx<n-1-layer; idx++) {
                buff = matrix[layer][idx];
                matrix[layer][idx] = matrix[n-1-idx][layer];
                matrix[n-1-idx][layer] = matrix[n-1-layer][n-1-idx];
                matrix[n-1-layer][n-1-idx] = matrix[idx][n-1-layer];
                matrix[idx][n-1-layer] = buff;
            }
        }
    }
}