""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    
    if not root :
        return False
    
    return check(root, -1, 10001)
    

def check(node, mi, ma):
    if not node :
        return True
    
    if mi and node.data<=mi :
        return False
    
    if ma and node.data>=ma :
        return False
    
    else :
        return check(node.left,mi,min(ma,node.data)) and check(node.right,max(mi,node.data),ma)
