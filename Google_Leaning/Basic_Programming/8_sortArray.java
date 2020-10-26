int[] sort(int[] a) {
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
    {
      fnl[index++]  = i+min;
    }
  }
  return fnl;
}
