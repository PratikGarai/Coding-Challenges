'''
from itertools import permutations 
  
def lexicographical_permutation(str): 
    perm = sorted(''.join(chars) for chars in permutations(str)) 
    for x in perm: 
        print(x) 
          
str ='bceghi'
lexicographical_permutation(str) 
'''
def foo(self):
        if self.isempty():
            return(0)
        elif self.isleaf():
            return(self.value)
        else:
            return(self.value + max(self.left.foo(),
                                    self.right.foo()))
