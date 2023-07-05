class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array) - 1]
    
    def push(self, data):
        self.array.append(data)

    def pop(self):
        if len(self.array) != 0:
            self.array.pop()
        else:
            print("Empty Stack")
    
    def print_stack(self):
        if len(self.array) == 0:
            print("Empty Stack")
            return
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])

my_stack = Stack()

my_stack.push("Andrei's")

my_stack.push("Courses")

my_stack.push("Are")

my_stack.push("Awesome")
# my_stack.print_stack()

my_stack.pop()
my_stack.pop()
# my_stack.print_stack()

# print(my_stack.peek())

print(my_stack.__dict__)

