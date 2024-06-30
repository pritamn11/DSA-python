class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def displayLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref

    def addBegin(self, data):
        new_node = Node(data)
        new_node.ref = self.head 
        self.head = new_node
    
    def addLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            

sll = SinglyLinkedList()
sll.addBegin(30)
sll.addBegin(20)
sll.addBegin(10)

sll.addLast(100)

sll.displayLinkedList()




