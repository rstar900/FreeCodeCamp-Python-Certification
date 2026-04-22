class HashTable:
    def __init__(self):
        self.collection = dict()

    def hash(self, key):
        result = 0
        for char in key:
            # Use ord() function to get the unicode value of the char
            result += ord(char)
        return result    
    
    def add(self, key, value):
        # Compute hash of the key
        hash_value = self.hash(key)
        # If the hash_value already exists, add it to the nested dictionary
        if hash_value in self.collection:
            self.collection[hash_value][key] = value
        # Otherwise create a new nested dictionary with hash_value as the key    
        else:
            self.collection[hash_value] = {key: value}

    def remove(self, key):
        # Compute hash of the key
        hash_value = self.hash(key)
        # If the hash_value already exists and the key as well, remove only the specific key
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]
        # No need to do anything in the else case   

    def lookup(self, key):
        # Compute hash of the key
        hash_value = self.hash(key)
        # Retrieve the value, only if the hash_value already exists and the key as well
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]
        # Otherwise return None
        return None             

