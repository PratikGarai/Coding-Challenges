
//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.io.*;

public class Main
{
    public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
		while(t-->0){
		    String inputLine[] = br.readLine().trim().split(" ");
		    int n = Integer.parseInt(inputLine[0]);
		    int m = Integer.parseInt(inputLine[1]);
		    long arr1[] = new long[n];
		    long arr2[] = new long[m];
		    inputLine = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++){
		        arr1[i] = Long.parseLong(inputLine[i]);
		    }
		    inputLine = br.readLine().trim().split(" ");
		    for(int i=0; i<m; i++){
		        arr2[i] = Long.parseLong(inputLine[i]);
		    }
		    Solution ob = new Solution();
		    ob.merge(arr1, arr2, n, m);
		    
		    StringBuffer str = new StringBuffer();
		    for(int i=0; i<n; i++){
		        str.append(arr1[i]+" ");
		    }
		    for(int i=0; i<m; i++){
		        str.append(arr2[i]+" ");
		    }
		    System.out.println(str);
		}
	}
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
    //Function to merge the arrays.
    public static void merge(long arr1[], long arr2[], int n, int m) 
    {
        int i=0, j=0, ind=0;
        long k=0;
        long[] arr3 = new long[m+n];
        while(i<n && j<m) {
            if(arr1[i]<arr2[j]) {
                arr3[ind++] = arr1[i++];
            } else {
                arr3[ind++] = arr2[j++];
            }
        }
        while(i<n) {
            arr3[ind++] = arr1[i++];
        }
        while(j<m) {
            arr3[ind++] = arr2[j++];
        }
        
        for(ind=0; ind<n; ind++){
            arr1[ind] = arr3[ind];
        }
        for(ind=0; ind<m; ind++){
            arr2[ind] = arr3[n+ind];
        }
    }
}



// ============================ SOLUTION 2 ======================================
//

//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.io.*;

public class Main
{
    public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
		while(t-->0){
		    String inputLine[] = br.readLine().trim().split(" ");
		    int n = Integer.parseInt(inputLine[0]);
		    int m = Integer.parseInt(inputLine[1]);
		    long arr1[] = new long[n];
		    long arr2[] = new long[m];
		    inputLine = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++){
		        arr1[i] = Long.parseLong(inputLine[i]);
		    }
		    inputLine = br.readLine().trim().split(" ");
		    for(int i=0; i<m; i++){
		        arr2[i] = Long.parseLong(inputLine[i]);
		    }
		    Solution ob = new Solution();
		    ob.merge(arr1, arr2, n, m);
		    
		    StringBuffer str = new StringBuffer();
		    for(int i=0; i<n; i++){
		        str.append(arr1[i]+" ");
		    }
		    for(int i=0; i<m; i++){
		        str.append(arr2[i]+" ");
		    }
		    System.out.println(str);
		}
	}
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
    static int radix=10000000;
    
    static void modifyAndStore(long arr1[], long arr2[], int n, int m, int ind, long val) {
        if(ind < n) {
            arr1[ind] = (val*radix) + arr1[ind];
        } else {
            arr2[ind-n] = (val*radix) + arr2[ind-n];
        }
    }
    
    static long get(long arr[], int ind, boolean original) {
        if(original) {
            return arr[ind] % radix;
        } else {
            return arr[ind] / radix;
        }
    }
    
    //Function to merge the arrays.
    public static void merge(long arr1[], long arr2[], int n, int m) 
    {
        int i=0, j=0, ind=0;
        long k=0;
        long[] arr3 = new long[m+n];
        while(i<n && j<m) {
            if(get(arr1,i,true) < get(arr2,j,true)) {
                modifyAndStore(arr1, arr2, n, m, ind, get(arr1,i,true));
                ind++;
                i++;
            } else {
                modifyAndStore(arr1, arr2, n, m, ind, get(arr2,j,true));
                ind++;
                j++;
            }
        }
        while(i<n) {
            modifyAndStore(arr1, arr2, n, m, ind, get(arr1,i,true));
            ind++;
            i++;
        }
        while(j<m) {
            modifyAndStore(arr1, arr2, n, m, ind, get(arr2,j,true));
            ind++;
            j++;
        }
        
        for(ind=0; ind<n; ind++){
            arr1[ind] = get(arr1, ind, false);
        }
        for(ind=0; ind<m; ind++){
            arr2[ind] = get(arr2, ind, false);
        }
    }
}
