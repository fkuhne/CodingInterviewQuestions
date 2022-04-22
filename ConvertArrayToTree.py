# Given an array, convert it to a balanced BST:

import math

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


def array2tree(array, start, end):
    if start > end: return None
    middle = math.ceil((start+end)/2)
#    print("middle = {}, root = {}".format(middle, array[middle]))
    root = tree(array[middle], array2tree(array, start, middle-1), array2tree(array, middle+1, end))
#    root.printTree()
#    print("\n")
    return root

a = [-10, -3, 0, 5, 9]
r = array2tree(a, 0, len(a)-1)

r.printTree()
