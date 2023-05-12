import java.util.Comparator;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public Integer[] createIndex(int n) {
        Integer[] indexes = new Integer[n];
        for(int i=0; i<n; i++) {
            indexes[i] = i;
        }
        return indexes;
    }

    public int[][] convertArrayListToArray(ArrayList<int[]> list) {
        int[][] res = new int[list.size()][2];
        int ind = 0;
        for(int[] element : list) {
            res[ind][0] = element[0];
            res[ind][1] = element[1];
            ind++;
        }
        return res;
    }

    public int[][] merge(int[][] intervals) {
        int l = intervals.length;
        Integer[] indexes = createIndex(l);
        Arrays.sort(indexes, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int[] i = intervals[a];
                int[] j = intervals[b];
                if(i[0] == j[0]) {
                    return i[1] - j[1];
                } else {
                    return i[0] - j[0];
                }
            }
        });

        ArrayList<int[]> resBuffer = new ArrayList<int[]>();

        int start = intervals[indexes[0]][0];
        int end = intervals[indexes[0]][1];
        int s, e;
        for(int i=0; i<l; i++) {
            s = intervals[indexes[i]][0];
            e = intervals[indexes[i]][1];
            if(start <= s && end >= e) {
                continue;
            } else if(start <= s && end >= s) {
                end = e;
            } else {
                int[] ele = new int[2];
                ele[0] = start;
                ele[1] = end;
                resBuffer.add(ele);
                start = s;
                end = e;
            }
        }
        int[] ele = new int[2];
        ele[0] = start;
        ele[1] = end;
        resBuffer.add(ele);
        return convertArrayListToArray(resBuffer);
    }
}
