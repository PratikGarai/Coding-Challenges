//{ Driver Code Starts
import java.io.*;
import java.util.*;

  public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        while (tc-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int[] arr = new int[n];
            String[] inputLine = br.readLine().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            System.out.println(new Solution().maxProduct(arr, n));
        }
    }
}

// } Driver Code Ends


class Solution {
    // Function to find maximum product subarray
    long maxProduct(int[] arr, int n) {
        int mxEle = -101;
        for(int i=0; i<n; i++) {
            mxEle = Math.max(arr[i], mxEle);
        }
        
        long mx=-101, pr=1;
        int left=0, right=0;
        while(right<n) {
            if(arr[right]==0) {
                while(left<right-1){
                    pr = pr/arr[left++];
                    mx = Math.max(mx, pr);
                }
                right++;
                left = right;
                pr = 1;
            } else {
               pr = pr*arr[right++];
               mx = Math.max(mx, pr);
            }
        }
        
        while(left<right-1){
            pr = pr/arr[left++];
            mx = Math.max(mx, pr);
        }
        return Math.max(mx, (long)mxEle);
    }
}
