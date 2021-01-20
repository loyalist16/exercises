# 树节点
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


# 前序遍历
def preorder_traversal(node: TreeNode):
    if not node:
        return

    print(node.value)
    preorder_traversal(node.left_child)
    preorder_traversal(node.right_child)


# 中序遍历
def inorder_traversal(node: TreeNode):
    if not node:
        return

    inorder_traversal(node.left_child)
    print(node.value)
    inorder_traversal(node.right_child)

# 后序遍历
def postorder_traversal(node: TreeNode):
    if not node:
        return
    postorder_traversal(node.left_child)
    postorder_traversal(node.right_child)
    print(node.value)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left_child = TreeNode(2)
    root.right_child = TreeNode(3)
    root.left_child.left_child = TreeNode(4)
    root.left_child.right_child = TreeNode(5)
    root.right_child.right_child = TreeNode(6)

    preorder_traversal(root)
    print('=======')
    inorder_traversal(root)
    print('========')
    postorder_traversal(root)
