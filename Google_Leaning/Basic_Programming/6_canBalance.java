public boolean canBalance(int[] nums) {
  int t_sum = 0;
  for(int s : nums)
    t_sum += s;
  if(t_sum%2!=0)
    return false;  
  t_sum = t_sum/2;
  for(int s : nums)
  {
    t_sum -= s;
    if(t_sum==0)
      return true;
    if(t_sum<0)
      return false;
  }
  return false;
}
