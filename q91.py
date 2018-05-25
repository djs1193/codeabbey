class Node:
 def __init__(self, value):
  self.value = value
  self.left = 0
  self.right = 0
 def __str__(self):
  if self.left:
   leftStr = str(self.left)
  else:
   leftStr = "-"
  if self.right:
   rightStr = str(self.right)
  else:
   rightStr = "-"
  return "("+leftStr+","+str(self.value)+","+rightStr+")"

nodes = []
inputstr = "10 15 9 5 12 11 19 21 23 2 18 4 1 3 14 17 7 24 13 6 20 8 22".split()
for i in inputstr:
    nodes.append(int(i))

root = Node(int(nodes.pop(0)))
while nodes:
 cur = int(nodes.pop(0))
 curNode = root
 while ((cur < curNode.value) and curNode.left) or ((cur > curNode.value) and curNode.right):
  if cur < curNode.value:
   curNode = curNode.left
  else:
   curNode = curNode.right
 if cur < curNode.value:
  curNode.left = Node(cur)
 else:
  curNode.right = Node(cur)
print(root)




#adjusted - by using hand :(
