from SLinkedListImplementation import LinkedList, Node

my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
print('\n')

def reverse(linkedlist):
    if linkedlist.length <= 1:
        return linkedlist
    else:
        first = linkedlist.head
        second = first.next
        linkedlist.tail = linkedlist.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        linkedlist.head.next = None
        linkedlist.head = first
        return linkedlist.print_list()



reversed_linked_list = reverse(my_linked_list)
