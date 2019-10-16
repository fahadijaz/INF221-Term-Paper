import math


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

    return a


def merge_sort(a, first_index, last_index):
    """Sorts a list using the 'merge-sort' algorithm."""
    if first_index < last_index:
        middle_index = (first_index + last_index) // 2
        merge_sort(a, first_index, middle_index)
        merge_sort(a, middle_index + 1, last_index)
        return merge(a, first_index, middle_index, last_index)


def parent(i):
    return math.floor((i-1) / 2)


def left_child(i):
    return 2 * i + 1


def right_child(i):
    


def build_max_heap(a):
    """Builds a max heap"""
    pass


def max_heapify(a):
    """Max-heapifies a list"""

    pass


def heap_sort(a):
    """Sorts a list using the 'heap-sort' algorithm."""
    build_max_heap(a)
    for i in range(len(a), 2, -1):
        a[1], a[i] = a[i], a[1]


def quick_sort(a):
    """Sorts a list using the 'quick-sort' algorithm."""
    pass


if __name__ == '__main__':
    unsorted = [-2, 3, 4, -4, 2, 0, 1, 5, -5, -3, -1]
    print(merge_sort(unsorted, 1, len(unsorted)) == sorted(unsorted))
