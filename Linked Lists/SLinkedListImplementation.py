class Node():
    def __init__(self, data):
        self.data = data  # data in node
        self.next = None  # pointer to next node
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    
    def traverseToIndex(self, index):
        counter = 0
        current_node = self.head
        while(counter != index):
            current_node = current_node.next
            counter += 1
        return current_node
    
    def insert(self, index, data):
        if index > self.length - 1:
            print("Inserting at the end of the list")
            self.append(data)
        
        elif index == 0:
            print("Inserting at the front of the list")
            self.prepend(data)
        
        else:
            new_node = Node(data)
            lead = self.traverseToIndex(index - 1)
            tempholder = lead.next
            lead.next = new_node
            new_node.next = tempholder
            self.length += 1
            return self.print_list()



    def removeIndex(self, index):
        if self.head == None:
            return print("Linked List is empty.")
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return self.print_list()
        if index>=self.length:
            return print("Entered wrong index!")
        lead = self.traverseToIndex(index-1)
        toberemoved = lead.next
        lead.next = toberemoved.next
        self.length -= 1
        return self.print_list()
    
    def print_list(self):
        if self.head == None:
            print("Empty List")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= '---->')
                current_node = current_node.next

# mylinkedlist = LinkedList()

# mylinkedlist.print_list()
# print('\n')

# mylinkedlist.append(4)

# mylinkedlist.print_list()
# print('\n')

# mylinkedlist.append(5)

# mylinkedlist.print_list()
# print('\n')

# mylinkedlist.prepend(3)

# mylinkedlist.print_list()
# print('\n')

# mylinkedlist.prepend(2)

# mylinkedlist.print_list()
# print('\n')

# mylinkedlist.insert(10, 9)

# mylinkedlist.print_list()
# print('\n')

# mylinkedlist.removeIndex(4)