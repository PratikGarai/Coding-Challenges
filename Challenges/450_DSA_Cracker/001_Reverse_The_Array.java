import java.util.* ;
import java.io.*; 
import java.util.ArrayList;

public class Solution 
{
    public static void reverseArray(ArrayList<Integer> arr, int m)
    {
        int beg = m + 1;
        int end = arr.size() - 1;
        int mid = (beg + end) / 2;
        int a, b;

        for(int i = beg; i < mid + 1; i++) {
            a = arr.get(i);
            b = arr.get(end - (i - beg));
            arr.set(i, b);
            arr.set(end - (i - beg), a);
        } 
    }
}
