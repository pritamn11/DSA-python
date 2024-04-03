class QueuesArray:
    def __init__(self):
        self._data=[]
    def __len__(self): # O(1)
        return len(self._data)
    def isempty(self): # O(1)
        return len(self._data)==0
    def enqueue(self,e): #O(1)
        self._data.append(e)
        return e
    def dequeue(self): # O(1)
        if self.isempty():
            return ValueError("")
        return self._data.pop(0) # O(1)
    def first(self): # O(1)
        if self.isempty():
            print ('Queue is empty')
        return self._data[0]
    

q = QueuesArray()    
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
# print(q.dequeue())
# print(q.dequeue())
# print(q.first())
# print(q.isempty())
# print(q._data)

