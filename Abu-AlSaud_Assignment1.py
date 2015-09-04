#User name: alab5455
#Name: Ali Abu AlSaud
#Date: 9/4/2015
#Assignment 1 GitHub and Python Review (Data Structures)

#1. Queue implementation

print "Testing the Queue:"

import Queue

myQueue = Queue.Queue()

for QueueInput in range(10):
	myQueue.put(QueueInput)		#enqueue 10 different elements on the Queue
		
while not myQueue.empty():
	print myQueue.get()		#printing the content of the Queue
	
#2. Stack Class Implementation

print "\nTesting the Stack:"

class Stack():
	
	#The Stack Class Constructor
	def __init__(myStack):
		myStack.items = []
	
	#A function that push an element to the Stack
	def push(myStack, item):
		return myStack.items.append(item)
		
	#A function that pop an element from the Stack
	def pop(myStack):
		return myStack.items.pop()
		
	#A function that return the size of the Stack
	def checkSize(myStack):
		return len(myStack.items)
	
	#A funtion that check whether the Stack is enpty or not	
	def empty(myStack):
		return myStack.items == []
		
newStack = Stack()

for stackInput in range(10):
	newStack.push(stackInput)		#Pushing 10 different elements into the Stack

while not newStack.empty():
	print newStack.pop()			#Printing out the Stack

print "\n"

#3. Binary Tree Class Implementation

print "Testing the Binary Tree: "

#Node Class that is going to be used on the Binary Tree Class
class Node():
	
	#The Node Class constructor, it takes two arguments, one for the key value and another one for the parent value
	def __init__(BT, integerKey, parent):
		BT.integerKey = integerKey
		BT.rightChild = None
		BT.leftChild = None
		BT.parent = parent
		
#The Binary Tree Class:
class binaryTree():
	
	#Binary Tree Class constructor
	def __init__(BT, Root):
		BT.root = Node(Root, None)
		BT.current = BT.root
		BT.added = False	#A flag to check whether we added a node or not
		BT.deleted = False	#A flag to check whether we deleted a node or not
		BT.R = Root		#A variable that stores the tree roots value
		BT.rightC = None	#This is the right child of the root, this is where the search stops
		BT.rightLeftValue = None	#A variable that stores the value of the left child of the right child of the root
		BT.rightLeftVisited = False	#A flag to indicate whether we visited the RightLeftChild or not, this is going to be used in order to stop searching for the node on the add method
		
	#Add method
	def add(BT, value, parentValue):
		#This first if statement is to store the value of the left child of the right child of the root, this is used to stop searching for the parent that we are searching for
		if BT.current.integerKey == BT.rightC:
			if BT.current.leftChild:
				BT.rightLeftValue = BT.current.leftChild.integerKey
			else:
				BT.rightLeftVisited = True
		#This is where we indicate that we visited the right-part of the tree
		if BT.current.integerKey == BT.rightLeftValue:
			BT.rightLeftVisited = True
		#Adding a node when we reach the parent that we are searching for
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
		#Moving to the left child when we did not find the parent
		if BT.current.leftChild:
			BT.current = BT.current.leftChild
			BT.added = False
			BT.add(value, parentValue)
		#Moving to the right child when we did not fing the parent on the left child
		if BT.current.rightChild:
			BT.current = BT.current.rightChild
			BT.added = False
			BT.add(value, parentValue)
		#This if statement is to indicate when the search is finished
		if BT.current.integerKey == BT.rightC and BT.rightLeftVisited == True:
			print "Parent not found"
		#This is to go back to the previous parent
		if BT.current.parent:
			BT.current = BT.current.parent
			return
	
	#Delete method
	def delete(BT, value):
		if BT.current.integerKey == value:
			#Do not delete any nodes if there exist a child to this specific node
			if BT.current.leftChild != None or BT.current.rightChild != None:
				print "Node not deleted, has children"
				return
			#This is the removing nodes part of the code
			else:
				if BT.current.parent.leftChild.integerKey == value:
					BT.current.parent.leftChild = None
				else:
					BT.current.parent.rightChild = None
				BT.current = BT.current.parent
				BT.deleted = True
				return
		#This part is to search on the left child side of the node
		if BT.current:
			if BT.current.leftChild:
				BT.current = BT.current.leftChild
				BT.delete(value)
		#This part is to search on the right side after finishing the left side of the parent
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
		#This is to go to the previous parent
		if BT.current:
			if BT.current.parent:
				BT.current = BT.current.parent
				return
		return
	
	#Printing method, it prints in a pre-order
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

#Graph class using dictionary
class graph():
	
	#Constructor
	def __init__(Graph):
		Graph.dictionary = {}
		
	#A method to add a vertex
	def addVertex(Graph, value):
		if Graph.dictionary.has_key(value):
			print "Vertex already exists"
		else:
			newDictionary = {value:[]}
			Graph.dictionary.update(newDictionary)
		
	#A method to connect two vertecies with each other
	def addEdge(Graph, value1, value2):
		if Graph.dictionary.has_key(value1) and Graph.dictionary.has_key(value2):
			Graph.dictionary.get(value1).append(value2)
			Graph.dictionary.get(value2).append(value1)
		else:
			print "One or more verticies not found."
		
	#A function that prints all the adjacents to a specific vertex
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
