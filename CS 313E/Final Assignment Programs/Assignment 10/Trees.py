#  File: Trees.py
#
#  Description: This module contains the Tree classes.
#
#  Student's Name: Kevin Achico, Nadeem Abha
#
#  Student's UT EID: ka6893, na4333
#
#  Course Name: CS 313E 
#
#  Date Created: 12/01/12
#
#  Date Last Modified: 12/04/12



# Code supplied in the notes
class BinaryTreeNode: 

    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    #accessors and mutators 
    def getValue(self):
        return self._value
    
    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right

    def setValue(self, value):
        self._value = value

    def setLeft(self, left):
        self._left = left

    def setRight(self, right):
        self._right = right

    def isLeafNode(self):
        return not self._left and not self._right



# To find a particular key value in a binary search tree,
# start at the root and trac a path downard int he tree guided by binary search tree property
class BinarySearchTree:

    def __init__(self, root=None):
        self._root = root

    def isEmpty(self):
        return self._root == None

    def setRoot(self, value):
        self._root = value

    def getRoot(self):
        return self._root

    def inorderAux(node):
        if node == None:
            return
        else:

            BinaryTree.inorderAux(node.getLeft())
            print (node.getValue(), end=" ")
            BinaryTree.inorderAux(node.getRight())

    def inorder(self):
        if self.isEmpty():
            print("The tree is empty.")
        else:
            BinaryTree.inorderAux(self._root)

    def insertAux(node, item):
        if node.getValue() > item:
            if not node.getLeft():
                newNode = BinaryTreeNode(item)
                node.setLeft( newNode )
            else:
                BinarySearchTree.insertAux( node.getLeft(), item )
        else:
            if not node.getRight():
                newNode = BinaryTreeNode(item)
                node.setRight(newNode)
            else:
                BinarySearchTree.insertAux( node.getRight(), item)

    def insert( tree, item ):
        if tree.isEmpty():
           tree.setRoot( BinaryTreeNode(item) )
        else:
           BinarySearchTree.insertAux(tree.getRoot() , item )

    def inTreeAux(node, value, count=0):
        if node.getValue() == value:
            count += 1
            return (True, count)
        elif node.getValue() > value:
            if not node.getLeft():
                count+= 1
                return (False, count)
            else:
                count += 1
                return BinarySearchTree.inTreeAux(node.getLeft(), value, count)

        else:
            if not node.getRight():
                count += 1
                return (False, count)
            else:
                count += 1
                return BinarySearchTree.inTreeAux(node.getRight(), value, count)
            
    def inTree(self, item):
        if self.isEmpty():
            return False
        else:
            return BinarySearchTree.inTreeAux( self.getRoot(), item )
        

    

    
