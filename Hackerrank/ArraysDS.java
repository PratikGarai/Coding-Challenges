import java.util.Scanner;

public class Solution 
{    
    static int[] reverseArray(int[] a) 
    {
        int temp, l = a.length;
        for(int i=0;i<l/2;i++)
        {
            temp = a[i];
            a[i] = a[l-1-i];
            a[l-1-i] = temp;
        }
        
        return a;
    }

    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int i=0;i<n;i++)
            a[i] = in.nextInt();
            
        int[] b = reverseArray(a);
        for(int i: b)
        System.out.print(i+" ");    
    }
}
