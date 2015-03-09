import collections #for queue function

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.type = None

class BinaryTree:

    def __init__(self):
        self.root = None


    def insert_node(self,root,element):
        if self.root is None:
            self.root = Node(element)
        else:

            if root is None:
                root = Node(element)
            elif root.data <= element:
                root.right = self.insert_node(root.right,element)
                root.type = "right"
            elif root.data > element:
                root.left = self.insert_node(root.left,element)
                root.type = "left"

        return root

    def PreOrder(self,root):
        if root is not None:
            print(root.data),
            print(root.type)
            if root.left is not None:
                self.PreOrder(root.left)
            if root.right is not None:
                self.PreOrder(root.right)



a = BinaryTree()
print("A")
a.insert_node(a.root,100)
a.insert_node(a.root,50)
a.insert_node(a.root,25)
a.insert_node(a.root,200)
a.insert_node(a.root,125)
a.insert_node(a.root,350)
a.PreOrder(a.root)
print
print("B")
b = BinaryTree()
b.insert_node(b.root,100)
b.insert_node(b.root,50)
b.insert_node(b.root,25)
b.insert_node(b.root,200)
b.insert_node(b.root,125)
b.insert_node(b.root,450)
b.PreOrder(b.root)
print

# class Queue:
#     def __init__(self):
#         self.items = []
# 
#     def isEmpty(self):
#         return self.items == []
# 
#     def enqueue(self, item):
#         self.items.insert(0,item)
# 
#     def dequeue(self):
#         return self.items.pop()
# 
#     def size(self):
#        return len(self.items)

def level_order_traversal_1(root):
    if root == None:
        return
  
    queues = [collections.deque(), collections.deque()]  #two double-ended queues or deques. 
    
    current_queue = queues[0]
    next_queue = queues[1]
    
    current_queue.append(root)
    level_number = 0
    
    while current_queue:
        temp = current_queue.popleft()
        print str(temp.data) + ",",
        
        if temp.left != None:
            next_queue.append(temp.left)
            
        if temp.right != None:
            next_queue.append(temp.right)
            
        if not current_queue:
            print
            level_number += 1
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]
    print
    
level_order_traversal_1(a.root)
            