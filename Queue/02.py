class Queue:
    def __init__(self):
        self.queue = []

    def displayQueue(self):
        print(self.queue)

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            e = self.queue.pop(0)   
            print("Remove element ",e)

    def peek(self):
        if not self.queue:
            print("Queue is empty")
        else:
            e = self.queue[0]
            print("Peek element :",e)
    
    def isEmpty(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def sizeOfQueue(self):
        print("Size of Queue :",len(self.queue))

    

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.displayQueue()
# q.dequeue()
# q.displayQueue()

