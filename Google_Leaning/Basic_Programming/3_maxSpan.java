public int maxSpan(int[] nums) {
  int l=nums.length,uniques,max_diff = 0;
  
  if(l==0)
    return 0;
  
  int min = nums[0], max=nums[0];  
  for(int i=0;i<l;i++)
  {
    if(nums[i]<min)
      min = nums[i];
    if(nums[i]>max)
      max = nums[i];
  }
  
  if(max==min)
    return l;
    
  uniques = max-min+1;
  int a[][] = new int[uniques][2];
  for(int i=0;i<uniques;i++)
  {
    a[i][0] = l-1;
    a[i][1] = 0;
  }
  for(int i=0;i<l;i++)
  {
    if(i<a[nums[i]-min][0])
      a[nums[i]-min][0] = i;
    if(i>a[nums[i]-min][1])
      a[nums[i]-min][1] = i;
  }
  for(int i=0;i<uniques;i++)
  {
    if((a[i][1]-a[i][0])>max_diff)
      max_diff = a[i][1]-a[i][0];
  }
  return max_diff+1;
}
