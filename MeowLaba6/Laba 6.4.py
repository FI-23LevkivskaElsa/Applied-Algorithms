import time
import sys
from Laba6 import *

#4: Ітеративний MergeSort з поділом на 10 частин
def merge_ten_parts(data, aux, left, middle, right, counters):
    index = [left] + middle + [right + 1]
    current_index = index[:-1]
    sorted_data = []

    while any(current_index[i] < index[i + 1] for i in range(len(current_index))):
        min_val, min_idx = float('inf'), -1
        for i in range(len(current_index)):
            if current_index[i] < index[i + 1]:
                counters["comparisons"] = counters["comparisons"] + 1
                if data[current_index[i]] < min_val:
                    min_val = data[current_index[i]]
                    min_idx = i

        sorted_data.append(min_val)
        current_index[min_idx] = current_index[min_idx] + 1
        counters["copies"] = counters["copies"] + 1

    for i, val in enumerate(sorted_data):
        aux[left + i] = val
        counters["copies"] = counters["copies"] + 1

    for i in range(left, right + 1):
        data[i] = aux[i]
        counters["copies"] = counters["copies"] + 1


def iterative_merge_sort_ten_parts(data):
    n = len(data)
    counters = {"comparisons": 0, "copies": 0}
    aux = data[:]
    start_time = time.time()

    size = 1
    while size < n:
        for left in range(0, n, size * 10):
            middle = [min(left + size * (i + 1) - 1, n - 1) for i in range(9)]
            right = min(left + size * 10 - 1, n - 1)
            merge_ten_parts(data, aux, left, middle, right, counters)
        size = size * 10

    end_time = time.time()
    counters["time"] = end_time - start_time
    counters["memory"] = sys.getsizeof(data) + sys.getsizeof(aux)
    return data, counters


size = 10

sorted_data = generate_sorted_data(size)
random_data = generate_random_data(size)
almost_sorted_data = generate_almost_sorted_data(size)
reversed_data = generate_reversed_data(size)
few_unique_data = generate_few_unique_data(size)

print_data(sorted_data, "Відсортовані дані")
print_data(random_data, "Випадкові дані")
print_data(almost_sorted_data, "Майже відсортовані дані")
print_data(reversed_data, "Відсортовані у зворотному порядку дані")
print_data(few_unique_data, "З кількома унікальними значеннями дані")

merge_sort_data1, counters1 = iterative_merge_sort_ten_parts(sorted_data)
merge_sort_data2, counters2 = iterative_merge_sort_ten_parts(random_data)
merge_sort_data3, counters3 = iterative_merge_sort_ten_parts(almost_sorted_data)
merge_sort_data4, counters4 = iterative_merge_sort_ten_parts(reversed_data)
merge_sort_data5, counters5 = iterative_merge_sort_ten_parts(few_unique_data)

print("ВАРІАНТ 1 'Рекурсивний MergeSort':")

print("Відсортований масив 1:", merge_sort_data1)
print("Статистика 1, коли дані відсортовані:", counters1)

print("Відсортований масив 2:", merge_sort_data2)
print("Статистика 2, коли дані випадкові:", counters2)

print("Відсортований масив 3:", merge_sort_data3)
print("Статистика 3, коли дані майже відсортовані:", counters3)

print("Відсортований масив 4:", merge_sort_data4)
print("Статистика 4, коли дані відсортовані у зворотньому порядку:", counters4)

print("Відсортований масив 5:", merge_sort_data5)
print("Статистика 5, коли дані з кількома унікальними значеннями:", counters5)


#x = [10, 100, 1000, 10000, 100000, 1000000]
#y1_1 = [46, 1001, 15501, 210001, 2650001, 32000001]
#y1_2 = [30, 600, 9000, 120000, 1500000, 18000000]
#y1_3 = [0.0, 0.0025, 0.0156, 0.3124, 3.86, 48.28]
#y1_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y2_1 = [48, 1154, 19346, 291595, 3919839, 49430851]
#y2_2 = [30, 600, 9000, 120000, 1500000, 18000000]
#y2_3 = [0.0097, 0.0025, 0.04686, 0.61, 7.47, 94.85]
#y2_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y3_1 = [46, 1012, 15871, 215557, 2736307, 32668336]
#y3_2 = [30, 600, 9000, 120000, 1500000, 18000000]
#y3_3 = [0.0, 0.0, 0.03, 0.328, 3.8, 48.39]
#y3_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y4_1 = [54, 1098, 16560, 221481, 2773692, 33325803]
#y4_2 = [30, 600, 9000, 120000, 1500000, 18000000]
#y4_3 = [0.0, 0.005, 0.016, 0.2967, 3.6, 45.95]
#y4_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y5_1 = [51, 1099, 17014, 229636, 2796924, 33520773]
#y5_2 = [30, 600, 9000, 120000, 1500000, 18000000]
#y5_3 = [0.0, 0.0, 0.04686, 0.61, 7.37, 93.78]
#y5_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

