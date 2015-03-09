#!/usr/bin/env python

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



ll1 = linked_list()

ll1.add_node(None)
ll1.add_node(8)
ll1.add_node(1)
ll1.add_node(5)

head1 = ll1.cur_node

ll2 = linked_list()

ll2.add_node(None)
ll2.add_node(3)
ll2.add_node(9)
ll2.add_node(2)

head2 = ll2.cur_node

ll1.list_print()
ll2.list_print()
print(head1.data)
print(head2.data)

def add_integers(integer1, integer2):
    
    result = None
    last = None
    carry = 0
    first = 0
    second = 0
    pNew = linked_list()
    while (integer1 != None or integer2 != None or carry > 0):
       # first = (0 if integer1 == None else integer1.data)
       # second = (0 if integer2 == None else integer2.data)
        if integer1 == None:
            first = 0
        else:
            first = integer1.data
        if integer2 == None:
            second = 0
        else:
            second = integer2.data  
        sum = first + second + carry
        pNew.add_node(sum % 10)
        carry = sum/10
        if result == None:
            result = pNew
        else:
            last.next = pNew
            
        last = pNew
        if integer1 != None:
            integer1 = integer1.next
            
        if integer2 != None:
            integer2 = integer2.next
            
    return result;

llresult = add_integers(head1, head2)
llresult.list_print()

