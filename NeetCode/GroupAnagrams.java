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

/**
    Create a key for each string by sorting it.
    Space : O(n)
    Complexity : O(n * (26 + k))

    Slower than previous solution. Time difference is caused due to log(k) vs 26.
 */
class Solution {
    public static String createKey(String s) {
        int[] counter = new int[26];
        for(int i =0; i<s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
        }
        String k = "";
        for(int i=0; i<26; i++){
            if(counter[i]<10) {
                k += "00"+Integer.toString(counter[i]);
            } else if(counter[i]<100) {
                k += "0"+Integer.toString(counter[i]);
            } else {
                k += "100";
            }
        }
        return k;
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

/**
    Create a key for each string by sorting it.
    Space : O(n)
    Complexity : O(n * 26 * k).
    Faster than solution 2 because of the use of StringBuilder.
 */
class Solution {
    public static String createKey(String s) {
        int[] counter = new int[26];
        for(int i =0; i<s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
        }
        StringBuilder sb = new StringBuilder();
        for (int count : counter) {
            sb.append('#').append(count);
        }
        return sb.toString();
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