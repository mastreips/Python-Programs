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
ll.add_node(7) 
ll.add_node(4)
ll.add_node(9)
ll.add_node(4)
ll.add_node(7)
ll.add_node(4)

ll.list_print()

head = ll.cur_node
print(head.data)
print(head.arbitrary)
print(head.next.data)

def remove_duplicates(head):
    
    if head == None:
        return head
    
    dup_set = set()  #built in function 
    
    dup_set.add(head.data)
    curr = head
    while curr.next != None:
        if curr.next.data in dup_set:
            curr.next = curr.next.next
        else:
            dup_set.add(curr.next.data)
            curr = curr.next
    
    return head

sorted_list = linked_list()
sorted_head = remove_duplicates(head)
sorted_list.cur_node = sorted_head
sorted_list.list_print()