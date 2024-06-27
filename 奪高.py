class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
#類似於C的struct用於建立節點，key是節點的值，left及right分別為該節點的左子節點及右子節點
def insert(root, key):
    if root is None:
        return TreeNode(key)
    #如果無根節點，則建立一個新節點當作根節點
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    #跟根節點比較，如果較大則跟此根節點的右子節點比較，較小則跟此根節點的左子節點比較，遞迴直到出現沒有節點可以比較的狀況則建立一個新的節點
    return root

def tree_height(root):
    if root is None:
        return 0
    #如果節點為空，則回傳高度為0
    else:
        left_height = tree_height(root.left)
        #遞迴地計算左子樹的高度，把值存入left_height
        right_height = tree_height(root.right)
        #遞迴地計算右子樹的高度，把值存入right_height
        return max(left_height, right_height) + 1
        # 因為此遞迴計算的是左子樹或右子樹的路徑長的max，所以還要再加上當前節點的高度，所以要加一
M = int(input())
#把input的值轉成int並用M儲存
values = [int(n) for n in input().split()]
#用value[]儲存一行用空格當分界的input然後轉成int
root = None
for value in values:
    root = insert(root, value)
#把input一個個insert到二元搜尋樹中
height = tree_height(root)
print(height)
