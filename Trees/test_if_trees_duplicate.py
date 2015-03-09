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

def are_identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    
    if root1 != None and root2 != None:
        return (root1.data == root2.data and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))
    return False

print
print(are_identical(a.root, b.root))