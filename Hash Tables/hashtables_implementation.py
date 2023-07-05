class HashTable:
    def __init__(self, size):
        self.bucket = size
        self.hashmap = [None] * self.bucket
    
    def __str__(self):
        return str(self.__dict__)
    
    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.bucket
        return hash
    
    def put(self, key, value):
        address = self._hash(key)
        if not self.hashmap[address]:
            self.hashmap[address] = [[key, value]]
        else:
            self.hashmap[address].append([key, value])
        print(self.hashmap)
    
    def get(self, key):
        address = self._hash(key)
        reference = self.hashmap[address]
        if reference:
            for i in range(len(reference)):
                if reference[i][0] == key:
                    return reference[i][1]
        return None

    def key(self):
        keysarrays = []
        for i in range(len(self.hashmap)):
            if len(self.hashmap[i]) > 1:
                for j in range(len(self.hashmap[i])):
                    keysarrays.append(self.hashmap[i][j][0])
            else:
                keysarrays.append(self.hashmap[i][0][0])
        print(keysarrays)
        return keysarrays



h = HashTable(3)
print(h)
h.put('grapes', 1)
h.put('apples', 10)
h.put('oranage', 300)
h.put('banana', 200)
print(h.get('banana'))
h.key()
# h.remove('apples')
# print(h)