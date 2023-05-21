//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

class Sorting
{
    public static void main (String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        long t = sc.nextLong();
        
        while(t-- > 0)
        {
            long n = sc.nextLong();
            long arr[] = new long[(int)n];
            
            for(long i = 0; i < n; i++)
             arr[(int)i] = sc.nextLong();
             
            System.out.println(new Solution().inversionCount(arr, n));
            
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
    static long splitter(long arr[], int left, int right, long temp[]) {
        if(right-left<=1) {
            return 0;
        }
        int mid = (left+right)/2;
        long count = 0;
        count += splitter(arr, left, mid, temp);
        count += splitter(arr, mid, right, temp);
        count += merger(arr, left, mid, right, temp);
        return count;
    }
    
    static long merger(long arr[], int left, int mid, int right, long temp[]) {
        long count = 0;
        int i = (int)left, j = (int)mid, ind = (int)left;
        while(i<mid && j<right) {
            if(arr[i] <= arr[j]) {
                temp[ind] = arr[i];
                i++;
                ind++;
            } else {
                temp[ind] = arr[j];
                count += mid-i;
                j++;
                ind++;
            }
        }
        while(i<mid) {
            temp[ind] = arr[i];
            i++;
            ind++;
        }
        while(j<right) {
            temp[ind] = arr[j];
            j++;
            ind++;
        }
        for(ind=left; ind<right; ind++) {
            arr[ind] = temp[ind];
        }
        return count;
    }
    
    static long inversionCount(long arr[], long N)
    {
        long[] temp = new long[(int)N];
        return splitter(arr, 0, (int)N, temp);
    }
}
