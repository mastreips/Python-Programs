class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node
        self.arbitrary = None #aribtrary pointer

class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data, arbitrary=None):
        new_node = node() # create a new node
        new_node.data = data
        new_node.arbitrary = arbitrary
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print node.data
            node = node.next


ll = linked_list()

ll.add_node(None)
ll.add_node(21, 7) #data = 21 and arbitrary = 7
ll.add_node(14)
ll.add_node(7, 14)

ll.list_print()

head = ll.cur_node
print(head.data)
print(head.arbitrary)
print(head.next.data)

def deep_copy_arbritrary_pointer(head):
    if head == None:
        return None

    current = head
    new_head = None
    new_prev = None
    ht = dict()
    new_node = linked_list()
    while current != None:
        new_node.add_node(current.data, current.arbitrary)
        
        if new_prev != None:
            new_prev.next = new_node
        else:
            new_head = new_node
            
        ht[current] = new_node
        
        new_prev = new_node
        current = current.next
        
    new_current = new_head
    
    while new_current != None:
        if new_current.arbitrary != None:
            node = ht[new_current.arbitrary]
            
            new_current.arbitrary = node
            
        new_current = new_current.next
        
    return new_head

deep_copy_arbritrary_pointer(head)