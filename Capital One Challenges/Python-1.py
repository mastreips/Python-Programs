#!/usr/bin/env python

class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print(node.data)
            node = node.next



ll = linked_list()

ll.add_node(None)
ll.add_node(28)
ll.add_node(21)
ll.add_node(14)
ll.add_node(7)


ll.list_print()

head = ll.cur_node
print(head.data)
print(head.next.data)

def reverse_iterative(head):
    if (head == None or
        head.next == None):
        return head

    list_to_do = head.next

    reversed_list = head
    reversed_list.next = None

    while (list_to_do != None):
        temp = list_to_do
        list_to_do = list_to_do.next

        temp.next = reversed_list
        reversed_list = temp

    return(reversed_list)

revhead = reverse_iterative(head)
print(revhead.data)
print(revhead.next.data)
