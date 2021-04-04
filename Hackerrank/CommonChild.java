import java.util.*;

public class Solution 
{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.nextLine();
        String s2 = scanner.nextLine();
        int l1=s1.length(), l2=s2.length();
        
        int mat[][] = new int[l1+1][l2+1];
        for(int i=1;i<=l1;i++)
        {
            for(int j=1;j<=l2;j++)
            {
                if(s1.charAt(i-1)==s2.charAt(j-1))
                    mat[i][j] = 1+mat[i-1][j-1];
                
                mat[i][j] = mat[i][j]>mat[i-1][j]?mat[i][j]:mat[i-1][j];
                mat[i][j] = mat[i][j]>mat[i][j-1]?mat[i][j]:mat[i][j-1];
            }
        }
        
        System.out.println(mat[l1][l2]);
        scanner.close();
    }
}
