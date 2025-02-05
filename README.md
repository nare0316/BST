💻 Binary Search Tree (BST) Implementation

This repository contains an implementation of a Binary Search Tree (BST) in Python. The BST supports several fundamental operations, including insertion, deletion, traversal, searching, and various utility methods.

📌 Features

- **Insertion**: Insert values into the tree.
- **Traversal**: In-order, Pre-order, and Post-order traversals.
- **Deletion**: Remove nodes from the tree.
- **Search**: Find whether a value exists in the tree.
- **Utility Methods**: 
  - Get the minimum and maximum elements.
  - Get the successor and predecessor of a node.
  - Get the height and size of the tree.
  - Check if the tree is empty.

## Class: `TreeNode`
The `TreeNode` class represents a node in the binary tree.
Attributes:
- `val`: The value of the node.
- `left`: A reference to the left child node.
- `right`: A reference to the right child node.
Methods:
- `__init__(val)`: Initializes a new node with a given value.

## Class: `BST`
The `BST` class represents the Binary Search Tree itself and contains all the tree-related operations.
Attributes:
- `root`: The root of the tree.
- `size`: The number of nodes in the tree.
Methods:
`__init__(self)`
Initializes the BST with an empty tree (root is `None` and size is 0).
`insert(self, node, val) -> TreeNode`
Inserts a new value into the tree at the correct position. Returns the root of the tree.
`pre_traverse(self, root)`
Performs a pre-order traversal (root, left, right) of the tree.
`in_traverse(self, root)`
Performs an in-order traversal (left, root, right) of the tree.
`post_traverse(self, root)`
Performs a post-order traversal (left, right, root) of the tree.
`remove(self, root, val) -> TreeNode`
Removes a node with the specified value from the tree. Handles all cases of node deletion (leaf node, one child, two children).
`search(self, val) -> bool`
Searches for a value in the tree iteratively and returns `True` if found, otherwise `False`.
`searchRecursion(self, root, val) -> bool`
Searches for a value in the tree recursively and returns `True` if found, otherwise `False`.
`getHeight(self, root)`
Returns the height of the tree. The height is defined as the length of the longest path from the root to a leaf node.
`getSize(self, root)`
Returns the size (number of nodes) of the tree.
`getMax(self, root)`
Returns the node with the maximum value in the tree.
`getMin(self, root)`
Returns the node with the minimum value in the tree.
`getSuccessor(self, root, val) -> TreeNode`
Finds and returns the successor of a node with the given value. The successor is the node with the smallest value greater than the given node's value.
`getPredecessor(self, root, val) -> TreeNode`
Finds and returns the predecessor of a node with the given value. The predecessor is the node with the largest value smaller than the given node's value.
`is_empty(self)`
Returns `True` if the tree is empty, otherwise `False`.

📌  Example Usage

```python
# Initialize BST
tree = BST()
# Insert elements
tree.insert(tree.root, 5)
tree.insert(tree.root, 3)
tree.insert(tree.root, 6)
tree.insert(tree.root, 2)
tree.insert(tree.root, 1)
# Traversals
print("In-order traversal:")
tree.in_traverse(tree.root)
print("\nPre-order traversal:")
tree.pre_traverse(tree.root)
print("\nPost-order traversal:")
tree.post_traverse(tree.root)
# Search for an element
found = tree.search(3)
print(f"Element found: {found}")
# Get the size and height of the tree
print(f"Tree size: {tree.getSize(tree.root)}")
print(f"Tree height: {tree.getHeight(tree.root)}")
# Get the maximum and minimum elements
print(f"Max element: {tree.getMax(tree.root).val}")
print(f"Min element: {tree.getMin(tree.root).val}")
# Remove a node
tree.remove(tree.root, 2)
print("\nAfter removal:")
tree.in_traverse(tree.root)
