
//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

public class GFG {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int k = Integer.parseInt(inputLine[1]);
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            int ans = new Solution().getPairsCount(arr, n, k);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution {
    int getPairsCount(int[] arr, int n, int k) {
        Integer t = new Integer(k);
        Map<Integer, Integer> mp = new HashMap<Integer, Integer>();
        for(int i=0; i<n; i++) {
            Integer key = new Integer(arr[i]);
            if(mp.containsKey(key)) {
                mp.put(key, mp.get(key)+1);
            } else {
                mp.put(key, 1);
            }
        }
        
        int count = 0;
        Iterator<Map.Entry<Integer, Integer>> ab = mp.entrySet().iterator();
        while(ab.hasNext()) {
            Map.Entry<Integer, Integer> e = ab.next();
            Integer key = e.getKey();
            if(mp.containsKey(t-key)) {
                int v1 = e.getValue(), v2 = mp.get(t-key);
                if(2*key == t) {
                    count += (v1 * (v2-1)) / 2;
                } else {
                    count += v1 * v2;
                }
                mp.put(key, 0);
                mp.put(t-key, 0);
            }
        }
        return count;
    }
}
