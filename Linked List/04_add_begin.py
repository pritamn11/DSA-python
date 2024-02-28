## Adding the element at the begining of the linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None 


class SinglyLinkedList:
    def __init__(self,head = None):
        self.head = head  
    
    # Traversing through linked list
    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head 
            while self.head is not None:
                print(self.head.data,"-->",end=" ")
                self.head = self.head.ref 

    def AddBegin(self,data):
        new_node = Node(data)  
        new_node.ref = self.head 
        self.head = new_node 
    


sll = SinglyLinkedList()

sll.AddBegin(10)
sll.AddBegin(20)
sll.AddBegin(30)
sll.printLinkedList()    
