/**
    Create a key for each string by sorting it.
    Space : O(n)
    Complexity : O(n * k log(k))
 */
class Solution {
    public static String createKey(String s) {
        char[] c= s.toCharArray();
        Arrays.sort(c);
        return new String(c);
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> h = new HashMap<String, List<String>>();
        String generatedKey = null;
        for(String s : strs) {
            generatedKey = createKey(s);
            if(h.containsKey(generatedKey)) {
                h.get(generatedKey).add(s);
            } else {
                h.put(generatedKey, new ArrayList<String>());
                h.get(generatedKey).add(s);
            }
        }    
        List<List<String>> result = new ArrayList<List<String>>();
        for(String key : h.keySet()) {
            result.add(h.get(key));
        }
        return result;
    }
}