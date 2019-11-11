import math


def merge(a, first_index, middle_index, last_index):
    """Merge function for use in merge sort."""
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


def merge_sort(a, first_index=0, last_index=None):
    """Sorts a list using the 'merge-sort' algorithm."""
    if last_index is None:
        last_index = len(a) - 1
    if first_index < last_index:
        middle_index = (first_index + last_index) // 2
        merge_sort(a, first_index, middle_index)
        merge_sort(a, middle_index + 1, last_index)
        return merge(a, first_index, middle_index, last_index)


def parent(i):
    """Returns the parent to a node in a heap."""
    return math.floor((i-1) / 2)


def left_child(i):
    """Returns the left child of a node in a heap."""
    return 2 * i + 1


def right_child(i):
    """Returns the right child of a node in a heap."""
    return 2 * i + 2


def max_heapify(a, i, heap_size):
    """Max-heapifies subtree of 'a' rooted at 'i'."""
    l = left_child(i)
    r = right_child(i)
    if l <= heap_size - 1 and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size - 1 and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest, heap_size)


def build_max_heap(a):
    """Builds a max heap"""
    heap_size = len(a)
    for i in range(math.floor(heap_size / 2), -1, -1):
        max_heapify(a, i, heap_size)


def heap_sort(a):
    """Sorts a list using the 'heap-sort' algorithm."""

    build_max_heap(a)
    heap_size = len(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heap_size -= 1
        max_heapify(a, 0, heap_size)


def partition(array, low, high):
    """DEFINE PARTITION FOR QUICKSORT"""
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low=0, high=None):
    """Sorts a list using the 'quick-sort' algorithm."""
    if high is None:
        high = len(array) - 1
    if low < high:
        part = partition(array, low, high)
        quick_sort(array, low, part - 1)
        quick_sort(array, part + 1, high)


if __name__ == '__main__':
    unsorted = [-2, 3, 4, -4, 2, 0, 1, 5, -5, -3, -1]
    unsorted_copy = [-2, 3, 4, -4, 2, 0, 1, 5, -5, -3, -1]
    heap_sort(unsorted)
    print(unsorted == sorted(unsorted_copy))
    print(unsorted)