import numpy as np
import timeit
import copy
import benchmarking
import matplotlib.pyplot as plt


np.random.seed(12235)
merge_sort_results = []
heap_sort_results = []
quick_sort_results = []

for i in range(1, 7):
    test_data = np.random.random((10**i, ))

    clock = timeit.Timer(stmt='sort_func(copy(data))',
                         globals={'sort_func': benchmarking.merge_sort,
                                  'data': test_data,
                                  'copy': copy.copy})

    n_ar, t_ar = clock.autorange()
    t = clock.repeat(repeat=7, number=n_ar)
    print(f"Merge sort minimum time for 10^{i}:",min(t))
    merge_sort_results.append(min(t))

    clock = timeit.Timer(stmt='sort_func(copy(data))',
                         globals={'sort_func': benchmarking.heap_sort,
                                  'data': test_data,
                                  'copy': copy.copy})

    n_ar, t_ar = clock.autorange()
    t = clock.repeat(repeat=7, number=n_ar)
    print(f"Heap sort minimum time: for 10^{i}", min(t))
    heap_sort_results.append(min(t))

    clock = timeit.Timer(stmt='sort_func(copy(data))',
                         globals={'sort_func': benchmarking.quick_sort,
                                  'data': test_data,
                                  'copy': copy.copy})

    n_ar, t_ar = clock.autorange()
    t = clock.repeat(repeat=7, number=n_ar)
    print(f"Quick sort minimum time for 10^{i}:", min(t))
    quick_sort_results.append(min(t))
    print("--------------------")

print("Merge sort:", merge_sort_results)
print("Heap sort:", heap_sort_results)
print("Quick sort:", quick_sort_results)

plt.plot(merge_sort_results)
plt.plot(heap_sort_results)
plt.plot(quick_sort_results)
plt.show()
