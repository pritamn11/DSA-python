class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_pair = None

class dict2:
    def __init__(self):
        self.key_value_pairs = None

    def __setitem__(self, key, value):
        if self.key_value_pairs is None:
            self.key_value_pairs = KeyValuePair(key, value)
        else:
            current_pair = self.key_value_pairs
            while current_pair is not None:
                if current_pair.key == key:
                    current_pair.value = value
                    return
                if current_pair.next_pair is None:
                    current_pair.next_pair = KeyValuePair(key, value)
                    return
                current_pair = current_pair.next_pair

    def __getitem__(self, key):
        current_pair = self.key_value_pairs
        while current_pair is not None:
            if current_pair.key == key:
                return current_pair.value
            current_pair = current_pair.next_pair
        raise KeyError(key)

    def __str__(self):
        pairs_str = []
        current_pair = self.key_value_pairs
        while current_pair is not None:
            pairs_str.append(f"'{current_pair.key}': {current_pair.value}")
            current_pair = current_pair.next_pair
        return "{" + ', '.join(pairs_str) + "}"

# Example usage:
obj = dict2()
obj['a'] = 1
obj['b'] = 2
obj['c'] = 3

print(obj['a'])  # Output: 1
print(obj['b'])  # Output: 2
print(obj)       # Output: {'a': 1, 'b': 2, 'c': 3}
