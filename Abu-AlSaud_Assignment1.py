#User name: alab5455
#Name: Ali Abu AlSaud
#Date: 9/4/2015
#Assignment 1 GitHub and Python Review (Data Structures)

#1. Queue implementation

print "Testing the Queue:"

import Queue

myQueue = Queue.Queue()

for QueueInput in range(10):
	myQueue.put(QueueInput)
		
while not myQueue.empty():
	print myQueue.get()
	
#2. Stack Class Implementation

print "\nTesting the Stack:"

class Stack():
	
	def __init__(myStack):
		myStack.items = []
	
	def push(myStack, item):
		return myStack.items.append(item)
		
	def pop(myStack):
		return myStack.items.pop()
		
	def checkSize(myStack):
		return len(myStack.items)
		
	def empty(myStack):
		return myStack.items == []
		
newStack = Stack()

for stackInput in range(10):
	newStack.push(stackInput)

while not newStack.empty():
	print newStack.pop()

print "\n"

#3. Binary Tree Class Implementation

print "Testing the Binary Tree: "

class Node():
	def __init__(BT, integerKey, parent):
		BT.integerKey = integerKey
		BT.rightChild = None
		BT.leftChild = None
		BT.parent = parent
		
class binaryTree():
	def __init__(BT, Root):
		BT.root = Node(Root, None)
		BT.current = BT.root
		BT.added = False
		BT.deleted = False
		BT.R = Root
		BT.rightC = None	#This is the right child of the root, this is where the search stops
		BT.rightLeftValue = None
		BT.rightLeftVisited = False
		
	def add(BT, value, parentValue):
		if BT.current.integerKey == BT.rightC:
			if BT.current.leftChild:
				BT.rightLeftValue = BT.current.leftChild.integerKey
			else:
				BT.rightLeftVisited = True
		if BT.current.integerKey == BT.rightLeftValue:
			BT.rightLeftVisited = True
		if BT.current.integerKey == parentValue:
			if BT.current.leftChild == None:
				BT.current.leftChild = Node(value, BT.current)
				BT.added = True
				BT.rightLeftVisited = False
				return
			elif BT.current.rightChild == None:
				if BT.current.integerKey == BT.R:
					BT.rightC = value
				BT.current.rightChild = Node(value, BT.current)
				BT.added = True
				BT.rightLeftVisited = False
				return
			else:
				print "Parent has two children, node not added"
				BT.added = False
				return		
		if BT.current.leftChild:
			BT.current = BT.current.leftChild
			BT.added = False
			BT.add(value, parentValue)
		if BT.current.rightChild:
			BT.current = BT.current.rightChild
			BT.added = False
			BT.add(value, parentValue)
		if BT.current.integerKey == BT.rightC and BT.rightLeftVisited == True:
			print "Parent not found"
		if BT.current.parent:
			BT.current = BT.current.parent
			return
	
	def delete(BT, value):
		if BT.current.integerKey == value:
			if BT.current.leftChild != None or BT.current.rightChild != None:
				print "Node not deleted, has children"
				return
			else:
				if BT.current.parent.leftChild.integerKey == value:
					BT.current.parent.leftChild = None
				else:
					BT.current.parent.rightChild = None
				BT.current = BT.current.parent
				BT.deleted = True
				return
		if BT.current:
			if BT.current.leftChild:
				BT.current = BT.current.leftChild
				BT.delete(value)
		if BT.current:
			if BT.current.rightChild:
				BT.current = BT.current.rightChild
				BT.delete(value)
				if BT.current == BT.root:
					if BT.deleted == False:
						print "Node not found."
					else:
						BT.deleted = False
					return
		if BT.current:
			if BT.current.parent:
				BT.current = BT.current.parent
				return
		return
	
	def printTree(BT):
		if BT.current:
			print (BT.current.integerKey)
			if BT.current.leftChild:
				BT.current = BT.current.leftChild
				BT.printTree()
			if BT.current.rightChild:
				BT.current = BT.current.rightChild
				BT.printTree()
			if BT.current.parent:
				BT.current = BT.current.parent
				return
		
newTree = binaryTree(5)
newTree.add(21, 5)
newTree.add(32, 5)
newTree.add(4, 21)
newTree.add(51, 21)
newTree.add(7, 4)
newTree.add(6, 32)
newTree.add(8, 32)
newTree.add(9, 4)
newTree.add(12, 6)
newTree.add(22, 6)
print "The tree before deleting any elements: "
newTree.printTree()
newTree.delete(51)
newTree.delete(22)
print "The tree after deleting two elements: "
newTree.printTree()

#4. Graph class Implementation

print "\nTesting the Graph: "

class graph():
	
	def __init__(Graph):
		Graph.dictionary = {}
		
	def addVertex(Graph, value):
		if Graph.dictionary.has_key(value):
			print "Vertex already exists"
		else:
			newDictionary = {value:[]}
			Graph.dictionary.update(newDictionary)
		
	def addEdge(Graph, value1, value2):
		if Graph.dictionary.has_key(value1) and Graph.dictionary.has_key(value2):
			Graph.dictionary.get(value1).append(value2)
			Graph.dictionary.get(value2).append(value1)
		else:
			print "One or more verticies not found."
		
	def findVertex(Graph, value):
		if Graph.dictionary.has_key(value):
			print "Value adjacent to {} are: ". format(value)
			for adjacent in Graph.dictionary.get(value):
				print "{}". format(adjacent)
		else:
			print "The value is not found"
		
myGraph = graph()	
for vertex in range(10):
	myGraph.addVertex(vertex)

myGraph.addEdge(1, 2)
myGraph.addEdge(1, 3)
myGraph.addEdge(2, 3)
myGraph.addEdge(1, 4)
myGraph.addEdge(1, 5)
myGraph.addEdge(3, 4)
myGraph.addEdge(6, 7)
myGraph.addEdge(8, 1)
myGraph.addEdge(9, 2)
myGraph.addEdge(8, 4)
myGraph.addEdge(0, 3)
myGraph.addEdge(0, 9)
myGraph.addEdge(4, 7)
myGraph.addEdge(2, 4)
myGraph.addEdge(5, 6)
myGraph.addEdge(9, 3)
myGraph.addEdge(5, 7)
myGraph.addEdge(5, 9)
myGraph.addEdge(0, 2)
myGraph.addEdge(9, 3)
myGraph.findVertex(1)
myGraph.findVertex(2)
myGraph.findVertex(0)
myGraph.findVertex(9)
myGraph.findVertex(6)
