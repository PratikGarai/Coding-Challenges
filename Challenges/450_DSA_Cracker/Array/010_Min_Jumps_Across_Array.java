//{ Driver Code Starts
import java.lang.*;
import java.io.*;
import java.util.*;
class GFG
 {
	public static void main (String[] args) throws IOException
	 {
	 
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        int t = Integer.parseInt(br.readLine()); 

        while(t-- > 0){
            int size = Integer.parseInt(br.readLine());
            String[] arrStr = ((String)br.readLine()).split("\\s+");
            int[] arr= new int[size];
            for(int i = 0;i<size;i++){
                arr[i] = Integer.parseInt(arrStr[i]);
            }
            System.out.println(new Solution().minJumps(arr));
        }
	 }
	 
}

// } Driver Code Ends


class Solution{
    static int minJumps(int[] arr){
        
        int l = arr.length;
        int reach = arr[0];
        int ind = 0;
        int steps = 1;
        
        while (reach < l-1) {
            int mx = 0;
            int mxind = -1;
            for(int i = ind+1; i < ind+1+arr[ind]; i++) {
                if(i+1+arr[i] > mx) {
                    mx = i+arr[i];
                    mxind = i;
                }
            }
            
            if(mx <= reach) {
                return -1;
            }
            
            reach = mx;
            ind = mxind;
            steps++;
        }
        
        return steps;
    }
}
