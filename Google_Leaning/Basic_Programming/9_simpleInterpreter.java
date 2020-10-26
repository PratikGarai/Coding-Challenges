public int interpret(int value, String[] commands, int[] args) {
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
