def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    less_than_pivot = [x for x in A[1:] if x <= pivot]
    greater_than_pivot = [x for x in A[1:] if x > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
A=[1,6,3,9,2,5]
print(quick_sort(A))