class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sortedLinkedList: #O(n) Linear time
    def __init__(self):
        self.head = None

    def sortedInsert(self, data):
        addingNode = Node(data)
        if self.head is None: # Empty Linked List
            addingNode.next = None
            self.head = addingNode
        elif self.head.data >= data:
            addingNode.next = self.head
            self.head = addingNode
        else:
            currentNode = self.head
            while currentNode.next is not None and currentNode.next.data < data:
                currentNode = currentNode.next

            addingNode.next = currentNode.next
            currentNode.next = addingNode
    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


sll = sortedLinkedList()
sll.sortedInsert(1)
sll.sortedInsert(3)
sll.sortedInsert(5)
sll.sortedInsert(8)
sll.sortedInsert(2)
sll.sortedInsert(9)
sll.sortedInsert(4)
sll.sortedInsert(6)
sll.sortedInsert(10)
sll.sortedInsert(1)

sll.printList()