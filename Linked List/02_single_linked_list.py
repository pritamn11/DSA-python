## Traversing method in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None 


class SinlgeLinkedList:
    def __init__(self):
        self.head = None
    
    # Traversing through linked list
    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.data)
                n = n.ref 


ll1 = SinlgeLinkedList()
ll1.printLinkedList()

