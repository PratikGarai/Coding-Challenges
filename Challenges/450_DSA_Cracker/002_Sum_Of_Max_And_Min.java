import java.util.* ;
import java.io.*; 
public class Solution {
  public static int sumOfMaxMin(int[] arr, int n) {
      int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
      for(int i=0; i<n; i++) {
        if(arr[i] > max) {
          max = arr[i];
        }
        if(arr[i] < min) {
          min = arr[i];
        }
      }

      return min + max;
  }
}
