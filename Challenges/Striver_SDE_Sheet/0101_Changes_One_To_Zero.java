/*
* Solution 1
* 1. Traverse
* 2. If you find 0, make all elements in same row and column -1, except for original 0s
* 3. Traverse again and convert -1s to 0s
*/

class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int replacement = Integer.MIN_VALUE+10;

        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {

                if(matrix[i][j]==0) {
                    // Make rows -1
                    for(int i2=0; i2<rows; i2++) {
                        if(i2!=i && matrix[i2][j] != 0) {
                            matrix[i2][j] = replacement;
                        }
                    }

                    // Make cols -1
                    for(int j2=0; j2<cols; j2++) {
                        if(j2!=j && matrix[i][j2] != 0) {
                            matrix[i][j2] = replacement;
                        }
                    }
                }
            }
        }

        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                if(matrix[i][j] == replacement) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}


/*
* Solution 2
* Store which rows and columns to zero out in 2 different single dimnsion arrays
*/

class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int[] r_zero = new int[rows];
        int[] c_zero = new int[cols];

        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                if(matrix[i][j]==0) {
                    r_zero[i] = 1;
                    c_zero[j] = 1;
                }
            }
        }

        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                if(r_zero[i] == 1 || c_zero[j] == 1) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}