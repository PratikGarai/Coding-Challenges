
//{ Driver Code Starts
import java.io.*;
import java.util.*;
class GFG
{
    public static void main(String args[])throws IOException
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int r = sc.nextInt();
            int c = sc.nextInt();
            
            int matrix[][] = new int[r][c];
            
            for(int i = 0; i < r; i++)
            {
                for(int j = 0; j < c; j++)
                 matrix[i][j] = sc.nextInt();
            }
            Solution ob = new Solution();
            ArrayList<Integer> ans = ob.spirallyTraverse(matrix, r, c);
            for (Integer val: ans) 
                System.out.print(val+" "); 
            System.out.println();
        }
    }
}
// } Driver Code Ends


class Solution
{
    //Function to return a list of integers denoting spiral traversal of matrix.
    static ArrayList<Integer> spirallyTraverse(int matrix[][], int r, int c)
    {
        ArrayList<Integer> res = new ArrayList<Integer>();
        int layers = Math.min(r, c)/2, layer = 0;
        
        while(layer<layers) {
            for(int i=layer; i<c-1-layer; i++) 
                res.add(new Integer(matrix[layer][i]));
            
            for(int i=layer; i<r-1-layer; i++) 
                res.add(new Integer(matrix[i][c-1-layer]));
            
            for(int i=c-1-layer; i>layer; i--)
                res.add(new Integer(matrix[r-1-layer][i]));
            
            for(int i=r-1-layer; i>layer; i--)
                res.add(new Integer(matrix[i][layer]));
            layer++;
        }
        
        if(r==c && r%2==1 && c%2==1)
            res.add(new Integer(matrix[r/2][c/2]));
        else if(r<c && r%2==1)
            for(int i=layer; i<c-layer; i++)
                res.add(new Integer(matrix[r/2][i]));
        else if(c<r && c%2==1)
            for(int i=layer; i<r-layer; i++)
                res.add(new Integer(matrix[i][c/2]));
        return res;
    }
}
