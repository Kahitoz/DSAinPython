class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def Iterative_Inorder_Treaversal(root):
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right
    return result


root = BinaryTree(1)
root.left = BinaryTree(7)
root.right = BinaryTree(9)
root.left.left = BinaryTree(2)
root.left.right = BinaryTree(6)
root.right.right = BinaryTree(9)
root.left.left.left = BinaryTree(5)
root.left.left.right = BinaryTree(11)
root.right.right.left = BinaryTree(5)
print(Iterative_Inorder_Treaversal(root))