def swap(a, b):
    return b, a

def print_array(arr):
    print(" ".join(map(str, arr)))

def shell_sort(arr):
    swap_count = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                swap_count += 1
                j -= gap
            arr[j] = temp

        gap //= 2

    print("\nTotal number of swaps:", swap_count)

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    
    arr = list(map(int, input("Enter the elements separated by space: ").split()))

    print("Initial array:", end=" ")
    print_array(arr)

    shell_sort(arr)

    print("Sorted array:", end=" ")
    print_array(arr)