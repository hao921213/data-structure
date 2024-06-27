class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def create_node(value):
    return Node(value)

def push(top, value):
    new_node = create_node(value)
    new_node.next = top
    return new_node

def pop(top):
    if top is None:
        print("堆疊已空，無法彈出元素")
        return top

    temp = top
    top = top.next
    print(f"彈出元素：{temp.data}")
    del temp
    return top

def print_stack(top):
    current = top
    while current is not None:
        print(current.data)
        current = current.next

def free_stack(top):
    current = top
    while current is not None:
        next_node = current.next
        del current
        current = next_node

stack_top = None

# 將數字推入堆疊
stack_top = push(stack_top, 10)
stack_top = push(stack_top, 20)
stack_top = push(stack_top, 30)

# 輸出堆疊
print("堆疊內容：")
print_stack(stack_top)

# 將頂部數字彈出堆疊
stack_top = pop(stack_top)

# 輸出堆疊
print("堆疊內容（彈出一個元素後）：")
print_stack(stack_top)

# 釋放堆疊的記憶體
free_stack(stack_top)
