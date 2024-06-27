def swap(a, b):
    return b, a

def print_array(arr):
    print(" ".join(map(str, arr)))

def heapify(arr, n, i, swap_count):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = swap(arr[i], arr[largest])
        swap_count[0] += 1
        print(f"Swap #{swap_count[0]}:", end=" ")
        print_array(arr)

        heapify(arr, n, largest, swap_count)

def heap_sort(arr):
    swap_count = [0]

    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i, swap_count)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = swap(arr[0], arr[i])
        swap_count[0] += 1
        print(f"Swap #{swap_count[0]}:", end=" ")
        print_array(arr)

        heapify(arr, i, 0, swap_count)

    print("\nTotal number of swaps:", swap_count[0])

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    
    arr = list(map(int, input("Enter the elements separated by space: ").split()))

    print("Initial array:", end=" ")
    print_array(arr)

    # 呼叫堆積排序函數
    heap_sort(arr)

    print("Sorted array:", end=" ")
    print_array(arr)