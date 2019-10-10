def merge(a, first_index, middle_index, last_index):
    n1 = middle_index - first_index + 1
    n2 = last_index - middle_index

    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = a[first_index + i - 1]

    for j in range(n2):
        right[j] = a[middle_index + j]

    left.append(float('inf'))
    right.append(float('inf'))

    i = 0
    j = 0

    for k in range(first_index - 1, last_index):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1


def merge_sort(a, first_index, last_index):
    """Sorts a list using the 'merge-sort' algorithm."""
    if first_index < last_index:
        middle_index = (first_index + last_index) // 2
        first_sorted = merge_sort(a, first_index, middle_index)
        last_sorted = merge_sort(a, middle_index + 1, last_index)
        merge()
    pass


def heap_sort(a):
    """Sorts a list using the 'heap-sort' algorithm."""
    pass


def quick_sort(a):
    """Sorts a list using the 'quick-sort' algorithm."""
    pass
