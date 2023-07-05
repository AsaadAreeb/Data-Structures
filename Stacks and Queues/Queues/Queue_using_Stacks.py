class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def peek(self):
        if len(self.s1) == 0:
            print("Empty")
        else:
            return self.s1[len(self.s1) - 1]

    def dequeue(self):
        if len(self.s1)==0:
            print("Queue Empty")
            return
        else:
            return self.s1.pop()
    
    def enqueue(self, data):
        for i in range(len(self.s1)):
            item = self.s1.pop()
            self.s2.append(item)
        self.s1.append(data)
        for i in range(len(self.s2)):
            item = self.s2.pop()
            self.s1.append(item)
        return
    
    def print_queue(self):
        if len(self.s1) == 0:
            print("Empty")
            return
        for i in range(len(self.s1) - 1, 0, -1):
            print(f'{self.s1[i]} <<-- ',end='')
        print(self.s1[0])
        return

my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(5)
my_queue.enqueue(0)
my_queue.print_queue()


my_queue.dequeue()
my_queue.print_queue()

print(my_queue.peek())