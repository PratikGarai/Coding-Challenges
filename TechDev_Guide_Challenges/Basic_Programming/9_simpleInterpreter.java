import java.util.Scanner;

class SimpleInterpreter
{
	public int interpret(int value, String[] commands, int[] args) 
	{
  		int val = value, l = commands.length;
  		for(int i=0;i<l;i++)
  		{
    			switch(commands[i].charAt(0))
    			{
      				case '+':
        				val += args[i];
        				break;
      				case '*':
        				val *= args[i];
        				break;
      				case '-':
        				val -= args[i];
        				break;
      				default :
        				return -1;
    			}
  		}
  		return val;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		SimpleInterpreter ob = new SimpleInterpreter();
		System.out.print("Enter the initial value : ");
		int value = in.nextInt();
		System.out.print("Enter the number of operators : ");
		int t = in.nextInt();
		
		String commands[] = new String[t];
		int arg[] = new int[t];
		for(int i=0;i<t;i++)
		{
			System.out.print("Enter the "+(i+1)+"th command : ");
			commands[i] = in.next();
			System.out.print("Enter the "+(i+1)+"th argument : ");
			arg[i] = in.nextInt();
		}

		System.out.println("The result : "+ob.interpret(value, commands, arg));

	}
}
