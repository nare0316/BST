class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root: TreeNode = None
        self.size = 0

    def insert(self, node, val)->TreeNode:
        if self.root == None:
            self.size += 1
            self.root = TreeNode(val)
            return self.root
        if node == None:
            self.size += 1
            return TreeNode(val)
        if val < node.val:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        return node

    def pre_traverse(self, root):
        if root == None:
            return
        print(root.val, end = ' ')
        self.pre_traverse(root.left)
        self.pre_traverse(root.right)
    
    def in_traverse(self, root):
        if root == None:
            return
        self.in_traverse(root.left)
        print(root.val, end = ' ')
        self.in_traverse(root.right)
        
    def post_traverse(self, root):
        if root == None:
            return
        self.post_traverse(root.left)
        self.post_traverse(root.right)
        print(root.val, end=" ")
        
        
    def remove(self, root, val)->TreeNode:
        if root == None:
            return None
        if val < root.val:
            root.left = self.remove(root.left, val)
        elif val > root.val:
            root.right = self.remove(root.right, val)
        else: 
            if not self.root.left and not self.root.right:
                self.size = 0
                self.root = None
                return self.root
            if root != self.root and not root.left:
                self.size -= 1
                return root.right
            if root != self.root and not root.right:
                self.size -= 1
                return root.left
            else:
                successor = self.getSuccessor(root, val)
                root.val = successor.val
                root.right = self.remove(root.right, successor.val)    
        return root
    
    def search(self, val)->bool:
        tmp = self.root
        while tmp:
            if val < tmp.val:
                tmp = tmp.left
            elif val > tmp.val:
                tmp = tmp.right
            else: 
                return True
        return False
            
    def searchRecursion(self, root, val)->bool:
        if root == None:
            return False
        if root.val == val:
            return True
        if val < root.val:
            return self.searchRecursion(root.left, val)
        
        else:
            return self.searchRecursion(root.right, val)
         
    def getHeight(self, root):
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return max(leftHeight, rightHeight) + 1
            
    def getSize(self, root):
        if not root:
            return 0
        leftSize = self.getSize(root.left)
        rightSize = self.getSize(root.right)
        return leftSize + rightSize + 1
    
    def getMax(self, root):
        tmp = root
        while tmp.right:
            tmp = tmp.right
        return tmp
    
    def getMin(self, root):
        tmp = root
        while tmp.left:
            tmp = tmp.left
        return tmp
    
    def getSuccessor(self, root, val)->TreeNode:
        tmp = root
        successor = None
        while val != tmp.val:
            if val < tmp.val:
                successor = tmp
                tmp = tmp.left
            else:
                tmp = tmp.right
    
        if tmp.right:
            return self.getMin(tmp.right)
        else:
            return successor
    
    def getPredecessor(self, root, val)->TreeNode:
        tmp = root
        predecessor = None
        while tmp.val != val:
            if val < tmp.val:
                tmp = tmp.left
            else:
                predecessor = tmp
                tmp = tmp.right
        if tmp.left:
            return self.getMax(tmp.left)
        else:
            return predecessor
        
    def is_empty(self):
        return self.root == None
        
        
    
tree = BST()

# tree.insert(tree.root, 5)
# tree.insert(tree.root, 3)
# tree.insert(tree.root, 6)
# tree.insert(tree.root, 2)
# tree.insert(tree.root, 1)
# tree.insert(tree.root, 100)
# tree.insert(tree.root, 7)
# tree.insert(tree.root, 4)
# tree.insert(tree.root, 7.5)
# tree.insert(tree.root, 6.5)
# print("pre")
# tree.pre_traverse(tree.root)
# print("\npost")
# tree.post_traverse(tree.root)
# print("\nThe max element is:", tree.getMax(tree.root).val)
# print("The min element is:", tree.getMin(tree.root).val)
# val = 6.5
# print(f"The successor of {val} is {tree.getSuccessor(tree.root, val).val}")
# print(f"The predecessor of {val} is {tree.getPredecessor(tree.root, val).val}")
# print(f"\nTree size is: {tree.size}")
# tree.in_traverse(tree.root)
# tree.remove(tree.root, 7)
# tree.remove(tree.root, 1)
# tree.remove(tree.root, 2)
# tree.remove(tree.root, 3)
# tree.remove(tree.root, 6)
# tree.remove(tree.root, 5)
# tree.remove(tree.root, 4)
# tree.remove(tree.root, 7.5)
# tree.remove(tree.root, 6.5)
# tree.remove(tree.root, 100)
# print(f"\nTree size is: {tree.size}")
# tree.in_traverse(tree.root)
# print()
# print(tree.searchRecursion(tree.root, 6.3))
# print(tree.getHeight(tree.root))
# print(tree.getSize(tree.root))
# print(tree.is_empty())
# tree.in_traverse(tree.root)




    
        


        
        

        
    