
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key)  :
        return self.data[key]  
    
    def __setitem__(self, key, value):
        self.data[key] = value
    

obj = MyList([1,2,5,6])
print(obj[2])  # 5

obj[1] = 'A'
obj[2] = 'B'
print(obj[2])   # B




