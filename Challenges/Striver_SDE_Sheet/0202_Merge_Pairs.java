/*
Sort the intervals given in ascending order to make it easier to merge.
Then, we can iterate through the intervals and merge them one by one.
*/

class Solution {
    public Integer[] generateIndex(int l) {
        Integer[] indexes = new Integer[l];
        for(int i=0; i<l; i++) {
            indexes[i] = i;
        }
        return indexes;
    }

    public int[][] merge(int[][] intervals) {
        int l = intervals.length;
        Integer[] indexes = generateIndex(l);
        Arrays.sort(indexes, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int[] first = intervals[a];
                int[] second = intervals[b];
                if(first[0] == second[0]) {
                    return first[1] - second[1];
                } else {
                    return first[0] - second[0];
                }
            }
        });

        ArrayList<int[]> buffer = new ArrayList<int[]>();
        int start = intervals[indexes[0]][0];
        int end = intervals[indexes[0]][1];
        int[] p;
        for(int i=0; i<l; i++) {
            p = intervals[indexes[i]];
            if(end < p[0]) {
                int pair[] = new int[]{start, end};
                buffer.add(pair);
                start = p[0];
                end = p[1];
            } else if (end < p[1]) {
                end = p[1];
            } else {
                continue;
            }
        }
        int pair[] = new int[]{start, end};
        buffer.add(pair);

        int result_len = buffer.size();
        int[][] res = new int[result_len][2];
        for(int i=0; i<result_len; i++) {
            pair = buffer.get(i);
            res[i][0] = pair[0];
            res[i][1] = pair[1];
        }

        return res;
    }
}