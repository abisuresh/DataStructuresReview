class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def create_tree():
    left_node = Tree(1)
    right_node = Tree(3)
    root_node = Tree(2, left_node, right_node)
    return root_node


def print_values_nodes_in_tree__traversal_preorder(input_tree):

    if input_tree is None:
        return None

    print(input_tree.data)
    print_values_nodes_in_tree__traversal_preorder(input_tree.left)
    print_values_nodes_in_tree__traversal_preorder(input_tree.right)


def print_values_nodes_in_tree__traversal_inorder(input_tree):

    if input_tree is None:
        return None

    print_values_nodes_in_tree__traversal_preorder(input_tree.left)
    print(input_tree.data)
    print_values_nodes_in_tree__traversal_preorder(input_tree.right)


def print_values_nodes_in_tree__traversal_postorder(input_tree):

    if input_tree is None:
        return None

    print_values_nodes_in_tree__traversal_preorder(input_tree.left)
    print_values_nodes_in_tree__traversal_preorder(input_tree.right)
    print(input_tree.data)


def iterative_tree_traversal(input_tree):
    node = input_tree
    stack = []
    while True:
        print(node)
        if node is None:
            return
        if node is not None:
            stack.append(node)
            print(node.data)
            node = node.left
            if node.left is None:
                left_node = stack.pop()
                print(left_node)
                root_node = stack.pop()
                node = root_node
                print(node)

            if node.right is None:
                # root_node = stack.pop()
                node = node.left


def calc_sum_tree(input_tree):
    return 0


new_tree = create_tree()
print("preorder")
print_values_nodes_in_tree__traversal_preorder(new_tree)
print("inorder")
print_values_nodes_in_tree__traversal_inorder(new_tree)
print("postorder")
print_values_nodes_in_tree__traversal_postorder(new_tree)

# print("break")
# iterative_tree_traversal(new_tree)
