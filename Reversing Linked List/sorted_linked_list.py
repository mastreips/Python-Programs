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
ll.add_node(11) 
ll.add_node(82)
ll.add_node(23)
ll.add_node(29)

ll.list_print()

head = ll.cur_node
print(head.data)
print(head.arbitrary)
print(head.next.data)

def sorted_insert(head, node):
    
    if node == None:
        return head
    
    if head == None or node.data <= head.data:
        node.next = head
        return node
    
    curr = head
    while curr.next != None and curr.next.data < node.data:
        curr = curr.next
        
    node.next = curr.next
    curr.next = node
    
    return head

def insertion_sort(head):
    
    sorted = None
    curr = head
    
    while curr != None:
        temp = curr.next
        sorted = sorted_insert(sorted, curr)
        curr = temp
        
    return sorted

sorted_list = linked_list()
sorted_head = insertion_sort(head)
sorted_list.cur_node = sorted_head
sorted_list.list_print()