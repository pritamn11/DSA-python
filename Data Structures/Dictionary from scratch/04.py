
class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class dict2:
    def __init__(self):
        self.key_value_pairs = None 

    def __setitem__(self, key, value):
        if self.key_value_pairs is None:
            self.key_value_pairs = KeyValue(key, value)
        else:
            n = self.key_value_pairs
            while n is not None:
                if n.key == key:
                    n.value = value
                    return
                if n.next is None:
                    n.next = KeyValue(key,value)
                    return
                n = n.next


obj = dict2
obj['a'] = 1
print(obj)