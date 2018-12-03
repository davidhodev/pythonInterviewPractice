# Binary Search Tree in Python
# Has functions of insert, find, preorder, postorder, and inorder

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, data):
        if self.value == data:
            return False # No duplicates in this tree
        elif self.value > data: # If data is less than the value, put it on the left side
            if self.left: #Checks if the node already has a left child
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        if self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.left:
                self.left.preorder()
            print(str(self.value))
            if self.right:
                self.right.preorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data): # Calls insert function in the Node class. Returns True or False
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data): # Checks if data is in the tree (True or False)
        if self.root:
            self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PREORDER: ")
        self.root.preorder()

    def postorder(self):
        print("POSTORDER: ")
        self.root.postorder()

    def inorder(self):
        print("INORDER: ")
        self.root.inorder()


bst = Tree()
bst.insert(10)
bst.insert(15)
bst.insert(7)
bst.insert(9)
bst.insert(13)
bst.insert(1100)
bst.insert(2)
bst.postorder()
bst.preorder()
bst.inorder()
