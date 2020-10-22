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
        s += t;
        tracking = false;
      }
    }
  }
  return s;
}
