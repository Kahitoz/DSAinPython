class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Iterative Approach to print the tree in inorder method
    
    def Iterative_Inorder_Traversal(self, root):
        # left -> root -> right
        pointer = root
        store_node = []
        while True:
            if pointer is not None:
                store_node.append(pointer)
                pointer = pointer.left
            elif store_node:
                pointer = store_node.pop()
                print(pointer.data, end=' ')
                pointer = pointer.right
            else:
                break

    def Iterative_Preorder_Traversal(self, root):
        # root -> left -> right
        pointer = root
        stack = []
        stack.append(pointer)
        while stack:
            pointer = stack.pop()
            print(pointer.data, end=' ')
            if pointer.left is not None:
                stack.append(pointer.left)
            if pointer.right is not None:
                stack.append(pointer.right)
            
        
                



root = BinaryTree('F')
node_1 = BinaryTree('B')
node_2 = BinaryTree('G')
node_3 = BinaryTree('A')
node_4 = BinaryTree('D')
node_5 = BinaryTree('C')
node_6 = BinaryTree('E')
node_7 = BinaryTree('I')
node_8 = BinaryTree('H')

# Connecting nodes                                  
root.left = node_1
root.right = node_2
node_1.left = node_3
node_1.right = node_4
node_4.left = node_5
node_4.right = node_6
node_2.right = node_7
node_7.left = node_8

root.Iterative_Inorder_Traversal(root)
print()
root.Iterative_Preorder_Traversal(root)