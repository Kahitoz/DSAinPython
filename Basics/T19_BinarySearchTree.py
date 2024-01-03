#BST -> The left subtree of a node contains only nodes with keys lesser than nodes key
# The right subtree should contain all the keys greater than the nodes keys
# The left subtree and right subtree each must also be a BST.

# Binary Search Tree -> 5 4 10 7 25 36 1 121

# Duplicate Values are not generally present in the BST but if it is present then it should be 
# in the left side of the node

from T18_IterativeTraversingBT import BinaryTree


class Create_Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def Recursive_Inorder_Binary_Tree(self, root):
    # left subtree -> root -> right subtree
        if root is not None:
            self.Recursive_Inorder_Binary_Tree(root.left)
            print(root.data, end = ' ')
            self.Recursive_Inorder_Binary_Tree(root.right) 
 
        

# Creating nodes
root = Create_Binary_Tree('F')
node_1 = Create_Binary_Tree('B')
node_2 = Create_Binary_Tree('G')
node_3 = Create_Binary_Tree('A')
node_4 = Create_Binary_Tree('D')
node_5 = Create_Binary_Tree('C')
node_6 = Create_Binary_Tree('E')
node_7 = Create_Binary_Tree('I')
node_8 = Create_Binary_Tree('H')

# Connecting nodes
root.left = node_1
root.right = node_2
node_1.left = node_3
node_1.right = node_4
node_4.left = node_5
node_4.right = node_6
node_2.right = node_7
node_7.left = node_8

# Printing the Tree

root.Recursive_Inorder_Binary_Tree(root)
