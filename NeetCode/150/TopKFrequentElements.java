/*
 * Standard count and sort solution.
 */
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

/*
 * Here, we maintain an inverse mapping of count -> list of numbers with that count.
 * The we lookup for counts from max to min and add the numbers to the result.
 */
 class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] result = new int[k];
        HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
        HashMap<Integer, List<Integer>> icounter = new HashMap<Integer, List<Integer>>();
        
        for(int num : nums) {
            if(counter.containsKey(num)) {
                counter.put(num, counter.get(num)+1);
            } else {
                counter.put(num, 1);
            }
        }

        int v = 0;
        int maxf = 0;
        for(int key : counter.keySet()) {
            v = counter.get(key);
            if(!icounter.containsKey(v))
                icounter.put(v, new ArrayList<Integer>());
            icounter.get(v).add(key);
            maxf = Math.max(maxf, v);
        }

        int count = 0;
        while(true) {
            if(icounter.containsKey(maxf)) {
                for(int r : icounter.get(maxf)) {
                    result[count++] = r;
                    if(count == k)
                        return result;
                }
            }
            if(maxf == -10000)
                break;
            maxf--;
        }

        return result;
    }
}