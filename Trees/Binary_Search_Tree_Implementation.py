class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while(True):
                if value < current_node.value:
                    # left
                    if current_node.left == None:
                        current_node.left = new_node
                        return 
                    else:
                        current_node = current_node.left
                elif value > current_node.value:
                    # right
                    if current_node.right == None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right

    
    def lookup(self, value):
        if self.root == None:
            return print("Nothing to look")
        current_node = self.root
        while (current_node):
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return print("Found")
        return print("Not here")


    def remove(self, value):
        if self.root == None:
            return print("There is nothing")
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value == current_node.value:

                # option 1: No right child
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        # if parent > current value, make current left child a left child of parent.
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        
                        # if parent < current value, make the current left child a right child of parent.
                        elif current_node.left > parent_node.value:
                            parent_node.right = current_node.left

                # option 2: right child which does not have a left child
                elif current_node.left.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left
                    
                        # if parent > current value, make current right child a left child of parent.
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        
                        # if parent < current value, make the current right child a right child of parent.
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right

                # option 3: right child that has a left child //////// Still needs some work
                else:
                  #find the Right child's left most child
                  leftmost = currentNode.right.left
                  leftmostParent = currentNode.right
                  while leftmost.left != None:
                      leftmostParent = leftmost
                      leftmost = leftmost.left

                  #Parent's left subtree is now leftmost's right subtree
                  leftmostParent.left = leftmost.right
                  leftmost.left = currentNode.left
                  leftmost.right = currentNode.right

                  if parentNode == None:
                      self.root = leftmost
                  else:
                      if currentNode.data < parentNode.data:
                          parentNode.left = leftmost
                      elif currentNode.data > parentNode.data:
                          parentNode.right = leftmost
            return True

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
                            #Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

tree.lookup(90)

# tree.print_tree()
