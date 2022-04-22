# Given two binary trees, tell whether they are equal:


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

def sameTrees(A, B):
    if A == None and B == None:
        return True
    if (A == None and B != None) or (A != None and B == None):
        return False

    if (A.data == B.data) and (sameTrees(A.l, B.l) == True) and (sameTrees(A.r, B.r) == True):
        return True

    return False


t1 = tree(5, tree(3, tree(20, tree(6, None, None), None), None), tree(10, tree(1, None, None), tree(15, tree(30, None, tree(9, None, None)), tree(8, None, None))))
t2 = tree(4, tree(5, tree(6, tree(7, None, None), None), None), None)

t3 = tree(5, tree(3, tree(20, tree(6, None, None), None), None), tree(10, tree(1, None, None), tree(15, tree(30, None, tree(9, None, None)), tree(8, None, None))))


t1.printTree()

print("\n\n")

print(sameTrees(t1, t3))

