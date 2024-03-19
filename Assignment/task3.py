
class CustomException(Exception):
    def __init__(self, key):
        super().__init__(f"Key '{key}' not found")


class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class dict2:
    def __init__(self):
        self.key_value_pairs = None 

    def __setitem__(self, key, value):
        new_pair = KeyValue(key,value)
        if self.key_value_pairs is None:
            self.key_value_pairs = new_pair
        else:
            n = self.key_value_pairs
            while n.next is not None:
                n = n.next
            n.next = new_pair

    def __str__(self):
        add_bracket = "{"
        n = self.key_value_pairs
        while n is not None:
            add_bracket += f" '{n.key}': {n.value} "
            n = n.next
        add_bracket = add_bracket.rstrip(",") + "}"
        return add_bracket
    
    def __getitem__(self, key):
        n = self.key_value_pairs
        while n is not None:
            if n.key == key:
                return n.value
            n = n.next
        raise CustomException(key)



obj = dict2()
if __name__ == "__main__":
    try:
        val = obj['a']
        print(val)
    except Exception as e:
        raise CustomException(e)
            

    
        