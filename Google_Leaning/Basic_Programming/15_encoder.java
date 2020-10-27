
public String[] encoder(String[] raw, String[] code_words) {
    
  Map<String, String> a = new HashMap<String, String>();
  int ind = 0;
  for(String s : raw)
  {
    if(!a.containsKey(s))
    {
      a.put(s,code_words[ind++]);
    }
  }
  
  String res[] = new String[raw.length];
  ind = 0;
  for(String s : raw)
  {
    res[ind++] = a.get(s);
  }
  return res;
}
