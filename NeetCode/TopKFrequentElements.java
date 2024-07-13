class Count implements Comparable<Count> {
    int key;
    int value;

    public Count(int k, int v) {
        this.key = k;
        this.value = v;
    }

    public int compareTo(Count b) {
        return this.value - b.value;
    }
}

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] result = new int[k];

        HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
        for(int num : nums) {
            if(counter.containsKey(num)) {
                counter.put(num, counter.get(num)+1);
            } else {
                counter.put(num, 1);
            }
        }

        ArrayList<Count> arr = new ArrayList<Count>();
        for(int key : counter.keySet()) {
            arr.add(new Count(key, counter.get(key)));
        }

        Collections.sort(arr, Collections.reverseOrder());
        for(int i=0; i<k; i++) {
            result[i] = arr.get(i).key;
        }

        return result;
    }
}