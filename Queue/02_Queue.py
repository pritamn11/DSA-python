
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None 
        self._size = 0

    def displayQueue(self):
        if self.head is None:
            print("Queue is empty")
            return
        else:
            n = self.head
            while n is not None:
                print("[",n.data,"]",end="->")
                n = n.next
            print('None')


    def enqueue(self,data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            self.tail = self.head
        else:
            self.tail.next = new_data
            self.tail = new_data
        self._size += 1
    
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print(self.head.data) 
            self.head = self.head.next
            self._size -= 1
            if self.head is None:
                self.tail = None 
            return
        
    def get_size(self):
        print("Size of Queue :",self._size)

    def peek(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print(self.head.data)      

    def isEmpty(self):
        print(self.head == None)

    


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.displayQueue()
queue.get_size()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.get_size()
queue.enqueue(100)
queue.displayQueue()