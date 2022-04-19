# https://app.codility.com/programmers/trainings/7/tree_longest_zig_zag/
# Compute the number of zigzags in a tree



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

ll = 0
rr = 1
maxZig = 0
first = True

def computeZig(prevDir, zig, tree):
  if tree is None: return

  global maxZig, ll, rr, first

  if zig > maxZig: maxZig = zig

  nextZig = 0
  if(first == True):
    first = False
    nextZig = zig
  else:
    nextZig = zig + 1

  if tree.l != None:
    if prevDir == rr: computeZig(1-prevDir, nextZig, tree.l)
    else: computeZig(prevDir, zig, tree.l)
  if tree.r != None:
    if prevDir == ll: computeZig(1-prevDir, nextZig, tree.r)
    else: computeZig(prevDir, zig, tree.r)

def solution(tree):

  global maxZig
  previousDir = 0

  computeZig(previousDir, 0, tree)

  print("zigzag is " + str(maxZig))


# (5, (3, (20, (6, None, None), None), None), (10, (1, None, None), (15, (30, None, (9, None, None), (8, None, None), 
# (5, (3, (20, (6, None, None), None), None), (10, (1, None, None), (15, (30, None, (9, None, None)), (8, None, None))))

t1 = tree(5, tree(3, tree(20, tree(6, None, None), None), None), tree(10, tree(1, None, None), tree(15, tree(30, None, tree(9, None, None)), tree(8, None, None))))
t2 = tree(4, tree(5, tree(6, tree(7, None, None), None), None), None)

t1.printTree()

print("\n\n")

solution(t1)

