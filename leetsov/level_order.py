
nodeList = []
if root == None: return nodeList

quene = []
quene.append(root)
quene2 = []
valList = []

while quene != []:
	node = quene.pop[0]
	valList.append(node.val)

	if node.left != None:
		quene2.append(node.left)
	if node.right != None:
		quene2.append(node.right)
	if quene == [] :
		quene = list



aList = [1,2]
if aList == [] :
	print "empty"
else:
	first = aList.pop(0)
	two = aList.pop(0)
	print first , two
	print aList
	print aList == []