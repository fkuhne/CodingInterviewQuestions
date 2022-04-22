# Invert (or mirror) a binary tree:


class tree:
  def __init__(self, data=-1, l=None, r=None):
    self.data = data
    self.l = l
    self.r = r

  def printTree(self):
    print("(", end="")
    if(self.data): print("{}, ".format(self.data), end="")
    if(self.l): 
      tree.printTree(self.l) 
      print(", ", end="")
    else: print("None, ", end="")
    if(self.r): tree.printTree(self.r) 
    else: print("None)", end="")
    if(self.l == None and self.r == None): print(")", end="")

def invertBinaryTree(t):
    if t is None: return None
    t.l, t.r = t.r, t.l
    return tree(t.data, invertBinaryTree(t.l), invertBinaryTree(t.r))
    
t1 = tree(5, tree(3, tree(20, tree(6, None, None), None), None), tree(10, tree(1, None, None), tree(15, tree(30, None, tree(9, None, None)), tree(8, None, None))))
t2 = tree(4, tree(5, tree(6, tree(7, None, None), None), None), None)

t1.printTree()
print()
invertBinaryTree(t1).printTree()
