def push(stack, value):
    stack.append(value)
    return stack

def pop(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return stack, None
    popped_value = stack.pop()
    print(f"Popped value: {popped_value}")
    return stack, popped_value

def print_stack(stack):
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack content:", *stack)

def free_stack(stack):
    stack.clear()

my_stack = []

# 將數字推入堆疊
my_stack = push(my_stack, 10)
my_stack = push(my_stack, 20)
my_stack = push(my_stack, 30)

# 輸出堆疊
print_stack(my_stack)

# 將頂部數字彈出堆疊
my_stack, popped_value = pop(my_stack)

# 輸出堆疊
print_stack(my_stack)

# 釋放堆疊的資源
free_stack(my_stack)
