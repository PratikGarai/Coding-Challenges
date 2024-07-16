/*
 * Explaination here : https://leetcode.com/problems/valid-sudoku/solutions/5534646/java-constant-space-and-time-beats-100-in-time/
 */
class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] sq = new boolean[9][9];
        byte v;
        for(int r=0; r<9; r++) {
            for(int c=0; c<9; c++) {
                if(board[r][c] == '.') {
                    continue;
                }
                v = (byte)(board[r][c] - '0');

                if(rows[r][v-1]) {
                    return false;
                } else {
                    rows[r][v-1] = true;
                }

                if(cols[c][v-1]) {
                    return false;
                } else {
                    cols[c][v-1] = true;
                }
                
                if(sq[(r/3)*3+(c/3)][v-1]){
                    return false;
                } else {
                    sq[(r/3)*3+(c/3)][v-1] = true;
                }
            }
        }
        return true;
    }
}