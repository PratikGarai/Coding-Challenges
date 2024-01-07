class Solution {

    public static List<Integer> getInitialRow(int level){
        List<Integer> l = new ArrayList<Integer>();
        l.add(1);

        for(int i=1; i<=level; i++) {
            l.add(0);
        }
        return l;
    }

    public List<List<Integer>> generate(int numRows) {
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for(int r=0; r<numRows; r++) {
            List<Integer> l = getInitialRow(r+1);
            result.add(l);
            if(r >= 1) {
                for(int i=1; i<=r; i++) {
                    System.out.println(i);
                    l.set(i, result.get(r-1).get(i-1) + result.get(r-1).get(i));
                }
                result.get(r-1).remove(r);
            }
        }
        result.get(numRows-1).remove(numRows);

        return result;
    }
}