class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        if self.top == None:
            return None
        return self.top.data
    
    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.top == None:
            print("Stack is Empty")
        else:
            popped = self.top
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None
            print(popped.data)

    def print_stack(self):
        if self.top == None:
            print("Stack is Empty")
        else:
            current_pointer = self.top
            while current_pointer != None:
                print(current_pointer.data)
                current_pointer = current_pointer.next

my_stack = Stack()
print(my_stack.peek())
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
print("Top data : ")
print(my_stack.top.data)
print("Bottom data : ")
print(my_stack.bottom.data)
print("Whole Stack : ")
my_stack.print_stack()
print("Popped data : ")
my_stack.pop()
print("Remaining Stack : ")
my_stack.print_stack()

# my_stack.pop()
# my_stack.pop()
# my_stack.print_stack()