class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

def create_node(value):
    return Node(value)

def create_queue():
    return Queue()

def enqueue(queue, value):
    new_node = create_node(value)

    if queue.rear is None:
        # 如果佇列為空，則新節點是第一個節點
        queue.front = new_node
        queue.rear = new_node
    else:
        # 否則將新節點連接到佇列的尾部
        queue.rear.next = new_node
        queue.rear = new_node

def dequeue(queue):
    if queue.front is None:
        print("佇列已空，無法出列")
        return

    temp = queue.front
    queue.front = queue.front.next

    if queue.front is None:
        # 如果出列後佇列變空，則將 rear 也設為空
        queue.rear = None

    print(f"出列元素：{temp.data}")
    del temp

def print_queue(queue):
    current = queue.front
    while current is not None:
        print(current.data)
        current = current.next

def free_queue(queue):
    while queue.front is not None:
        dequeue(queue)
    del queue

def main():
    my_queue = create_queue()

    # 將數字入列
    enqueue(my_queue, 10)
    enqueue(my_queue, 20)
    enqueue(my_queue, 30)

    # 輸出佇列
    print("佇列內容：")
    print_queue(my_queue)

    # 出列
    dequeue(my_queue)

    # 輸出佇列
    print("佇列內容（出列一個元素後）：")
    print_queue(my_queue)

    # 釋放佇列的記憶體
    free_queue(my_queue)

if __name__ == "__main__":
    main()
