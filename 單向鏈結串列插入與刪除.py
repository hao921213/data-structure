# 定義員工結構
class Employee:
    def __init__(self, num, score, name):
        self.num = num
        self.score = score
        self.name = name
        self.next = None

# 尋找特定員工編號的節點
def find_node(head, num):
    ptr = head
    while ptr is not None:
        if ptr.num == num:
            return ptr
        ptr = ptr.next
    return ptr

# 插入節點
def insert_node(head, ptr, num, score, name):
    insert_node = Employee(num, score, name)
    if ptr is None:
        # 插入到鏈結串列開頭
        insert_node.next = head
        return insert_node
    else:
        if ptr.next is None:
            # 插入到鏈結串列末尾
            ptr.next = insert_node
        else:
            # 插入到鏈結串列中間
            insert_node.next = ptr.next
            ptr.next = insert_node
    return head

# 刪除節點
def delete_node(head, delete_num):
    current = head
    previous = None

    # 檢查是否為串列首
    if head is not None and head.num == delete_num:
        current = head
        head = head.next
        return head

    current = head
    previous = None

    # 尋找欲刪除節點
    while current is not None and current.num != delete_num:
        previous = current
        current = current.next

    # 找到欲刪除節點
    if current is not None:
        if previous is not None:
            previous.next = current.next
        return head
    else:
        print("找不到要刪除的節點")
        return head

# 釋放鏈結串列的記憶體
def free_linked_list(head):
    current = head
    next_node = None

    while current is not None:
        next_node = current.next
        current = next_node

# 初始化員工資料
data = [[1001, 32367], [1002, 24388], [1003, 27556], [1007, 31299], [1012, 42660], [1014, 25676],
        [1018, 44145], [1043, 52182], [1031, 32769], [1037, 21100], [1041, 32196], [1046, 25776]]
namedata = ["Allen", "Scott", "Marry", "John", "Mark", "Ricky", "Lisa", "Jasica", "Hanson", "Amy", "Bob", "Jack"]

# 創建鏈結串列
head = Employee(data[0][0], data[0][1], namedata[0])
ptr = head

for i in range(1, len(data)):
    new_node = Employee(data[i][0], data[i][1], namedata[i])
    ptr.next = new_node
    ptr = ptr.next

# 插入新節點或刪除節點
while True:
    print("\n")
    print("要插入其後的員工編號，如輸入的員工編號不在此串列中")
    print("新輸入的員工節點將視為此串列的串列首，要結束插入過程，請輸入-1：")
    print("要刪除的員工編號，要結束刪除過程，請輸入-2：")
    position = int(input())

    if position == -1:
        break
    elif position == -2:
        # 刪除節點
        print("請輸入要刪除的員工編號：")
        delete_num = int(input())
        head = delete_node(head, delete_num)
    else:
        # 插入新節點
        ptr = find_node(head, position)
        print("請輸入新插入的員工編號：")
        new_num = int(input())
        print("請輸入新插入的員工薪水：")
        new_score = int(input())
        print("請輸入新插入的員工姓名：")
        new_name = input()
        head = insert_node(head, ptr, new_num, new_score, new_name)

# 顯示最終的鏈結串列
ptr = head
print("\n\t員工編號\t姓名\t薪水\n")
print("\t===================================================================================================")
while ptr is not None:
    print("\t[%2d]\t[ %-7s]\t[%3d]" % (ptr.num, ptr.name, ptr.score))
    ptr = ptr.next

# 釋放鏈結串列的記憶體
free_linked_list(head)

