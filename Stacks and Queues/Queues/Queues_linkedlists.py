class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        if self.first == None:
            return print("Empty")
        else:
            return self.first.data
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        self.printt()

    def dequeue(self):
        if self.first == None:
            return print("Empty")
        else:
            de = self.first
            self.first = self.first.next
            self.length -= 1
            if self.length == 0:
                self.last = None
            print("Popped", de.data)
            self.printt()



    def printt(self):
        temp = self.first
        while temp != None:
            print(temp.data , end = '->')
            temp = temp.next
        print()
        print(self.length)


my_queue = Queue()

# my_queue.peek()

my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')
my_queue.enqueue('Samir')
my_queue.peek()

my_queue.dequeue()



