import java.util.Scanner;

class WithoutString
{
	public String withoutString(String base, String remove) 
	{
		int lb = base.length(), lr = remove.length();

  		if(lr>lb)
    			return base;

  		String s="",t="";
  		int tr_index = 0;
  		boolean tracking = false;
  		for(int i=0;i<lb;i++)
  		{
    			if(!tracking)
    			{
      				if(Character.toUpperCase(base.charAt(i))==Character.toUpperCase(remove.charAt(0)))
      				{
        				tracking = true;
        				t += remove.charAt(tr_index);
        				tr_index++;
      				}
      				else
      				{
        				s += base.charAt(i);
      				}
    			}
    			else
    			{
      				if(tr_index==lr)
      				{
			        	t = "";
        				tr_index = 0;
	        			tracking = false;
        				i--;
     			 	}
      				else if(Character.toUpperCase(base.charAt(i))==Character.toUpperCase(remove.charAt(tr_index)))
     	 			{
		        	 	t += remove.charAt(tr_index);
	        		 	tr_index++;
      				}
      				else
      				{
				        tr_index=0;
				        s += t+base.charAt(i);
				        tracking = false;
      				}
    			}
  		}
	  	if(tracking&&tr_index!=lr)
  		{
    			s += base.charAt(lr-1);
	  	}
  		return s;
	}

	public static void main(String[] args)
	{
		WithoutString ob = new WithoutString();
		Scanner in = new Scanner(System.in);
		String b,r;
		System.out.println("Enter the base string");
		b = in.nextLine();
		System.out.println("Enter the substring to be removed");
		r = in.nextLine();
		System.out.println("The result : "+ob.withoutString(b,r));
	}
}
