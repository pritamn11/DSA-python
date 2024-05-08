
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def displayQueue(self):
        if self.head is None:
            print("Queue is empty")
            return 
        else:
            n = self.head
            while n is not None:
                print(n.data,'-->',end=" ")
                n = n.next
            print('null')
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print(self.head.data) 
            self.head = self.head.next
    
    def peek(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print(self.head.data)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.displayQueue()

q.dequeue()
q.displayQueue()
q.peek()