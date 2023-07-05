class MyArray:

    def __init__(self):
        self.length = 0
        self.data = {}
    
    def get(self, index):
        return self.data[index]
    
    def __str__(self):
        return str(self.__dict__) 

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
    
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    
    def delete(self, index):
        self.shifItems(index)
        del self.data[self.length - 1]
        self.length -= 1

    
    def shifItems(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

    def insert(self, index, item):
        self.length += 1
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = item
    

    

myarray = MyArray()
myarray.push("hi")
myarray.push("hey")
myarray.push("yo")
myarray.push("my my")
print(myarray)
# print(myarray.pop())
# myarray.delete(1)
myarray.insert(2, "yo1")
print(myarray)
