class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if key < node.val:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current


def sum_nodes(node):
    if node is None:
        return 0
    return node.val + sum_nodes(node.left) + sum_nodes(node.right)


if __name__ == "__main__":
    # Test
    root_node = Node(5)
    root_node = insert(root_node, 3)
    root_node = insert(root_node, 2)
    root_node = insert(root_node, 4)
    root_node = insert(root_node, 7)
    root_node = insert(root_node, 6)
    root_node = insert(root_node, 8)

    print(max_value_node(root_node))
    print(min_value_node(root_node))
    print(sum_nodes(root_node))
