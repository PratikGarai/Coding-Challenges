import java.util.Scanner;
import java.util.Stack;

class Hello
{
	public static int Shape(String []arr,int n,int m)
	{
	   boolean[][] visited = new boolean[n][m];
	   int count = 0;
	   int[] dx = {-1,0,1,0};
	   int[] dy = {0,1,0,-1};
	   int nx,ny,x,y;
	   for(int i=0;i<n;i++)
	   {
	       for(int j=0;j<m;j++)
 	      {
	           if(visited[i][j])
       		     continue;
	           visited[i][j] = true;
	           if(arr[i].charAt(j)=='X')
	           {
	               count++;
	               Stack<Integer> stck1 = new Stack<Integer>();
	               Stack<Integer> stck2 = new Stack<Integer>();
               
	               stck1.push(i);
	               stck2.push(j);
               
	               while(!stck1.empty())
	               {
	                   x = stck1.pop();
	                   y = stck2.pop();
	                   for(int z=0;z<4;z++)
	                   {
	                        nx = x+dx[z];
        	                ny = y+dy[z];
                	        if(nx>=0 && nx<n && ny>=0 && ny<m)
                        	{
	                            if(!visited[nx][ny] && arr[nx].charAt(ny)=='X')
        	                    {
					visited[nx][ny] = true;
                	                stck1.push(nx);
                        	        stck2.push(ny);
                            	    }
                        	}
                   	    }
               		}
          	    }
       		}
	   }
   
   	   return count;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in); 
		int n = in.nextInt();
		int m = in.nextInt();
		String[] arr = new String[n];
		for(int i=0;i<n;i++)
		{
			arr[i] = in.next();
		}
		System.out.println(Shape(arr,n,m));
	}
}
