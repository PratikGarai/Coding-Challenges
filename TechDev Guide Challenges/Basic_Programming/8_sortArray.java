import java.util.Scanner;

class SortArray
{
	int[] sort(int[] a) 
	{
  		int l = a.length;
  		if(l==0)
    			return a;
  		int min = a[0], max = a[0];
  		for(int i=1;i<l;i++)
  		{
    			if(a[i]<min)
      				min = a[i];
    			if(a[i]>max)
      				max = a[i];
  		}
  		int arr[] = new int[max-min+1];
  		int unq = 0;
  		for(int i=0;i<l;i++)
  		{
    			if(arr[a[i]-min]==0)
    			{
      				unq++;
      				arr[a[i]-min] = 1;
    			}
  		}
  		int fnl[] = new int[unq];
  		int index=0;
  		for(int i=0;i<max-min+1;i++)
  		{
    			if(arr[i]==1)
      				fnl[index++]  = i+min;
  		}
  		return fnl;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		SortArray ob = new SortArray();
		System.out.print("Enter the number of elements : ");
		int n = in.nextInt();
		int a[] = new int[n];
		for(int i=0;i<n;i++)
		{
			System.out.print("Enter the "+(i+1)+"th element : ");
			a[i] = in.nextInt();
		}
		int b[] = ob.sort(a);
		System.out.print("\nThe result : ");
		for(int i : b)
			System.out.print(i+" ");
	}
}
