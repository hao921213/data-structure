class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# 深度優先遍歷（前序遍歷）
def preorder(root):
    if root is not None:
        # 先訪問當前節點的數據
        print(root.data, end=" ")

        # 遞歸訪問左子樹
        preorder(root.left)

        # 遞歸訪問右子樹
        preorder(root.right)

# 中序遍歷
def inorder(root):
    if root is not None:
        # 遞歸訪問左子樹
        inorder(root.left)

        # 訪問當前節點的數據
        print(root.data, end=" ")

        # 遞歸訪問右子樹
        inorder(root.right)

# 後序遍歷
def postorder(root):
    if root is not None:
        # 遞歸訪問左子樹
        postorder(root.left)

        # 遞歸訪問右子樹
        postorder(root.right)

        # 訪問當前節點的數據
        print(root.data, end=" ")

# 創建二元樹
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

    # 印出深度優先遍歷的結果
print("深度優先遍歷結果（前序遍歷）：", end="")
preorder(root)
print()

    # 印出中序遍歷的結果
print("中序遍歷結果：", end="")
inorder(root)
print()

 # 印出後序遍歷的結果
print("後序遍歷結果：", end="")
postorder(root)
print()