
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None 


class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def displayLinkedList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref 
    
    def addEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            return
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def addBegin(self,data):
        new_node = Node(data)
        new_node.ref = self.head 
        self.head = new_node

    def addAfter(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref 
        if n is None:
            print("Node value not exist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def addBefore(self,data,x):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head 
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node value not exist")
            else:
                new_node = Node(data)
                new_node.ref = n.ref 
                n.ref = new_node

    def addEmpty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")
   
    
    def deleteFirstNode(self):
        if self.head is None:
            print("Linked list is empty can't delete first node")
        else:
            self.head = self.head.ref

    def deleteLastNode(self):
        if self.head is None:
            print("Linked list is empty can't delete last node")
        elif self.head.ref is None:
            self.head = None    
        else:
            n = self.head 
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None 

    def deleteNodeValue(self,x):
        if self.head is None:
            print("Linked list is empty can't delete node")
        elif self.head.data == x:
            self.head = self.head.ref
            return
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref 
            if n.ref is None:
                print("Node value not exist")
            else:
                n.ref = n.ref.ref 


        



sll = SinglyLinkedList()
sll.addEnd(10)
sll.addEnd(20)
sll.addEnd(30)
sll.addEnd(40)
sll.addBegin(1)
sll.addBegin(2)
sll.addAfter(11,10)
sll.addBefore(12,20)
sll.deleteFirstNode()
sll.deleteFirstNode()
sll.deleteLastNode()
sll.deleteNodeValue(12)
sll.deleteNodeValue(10)
sll.displayLinkedList()