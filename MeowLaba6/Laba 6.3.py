import time
import sys
from Laba6 import *

#3: Ітеративний MergeSort з оптимізаціями
def cutoff_to_insertion(data, left, right):
    for i in range(left + 1, right + 1):
        key = data[i]
        j = i - 1
        while j >= left and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def eliminate_the_copy_to_the_auxiliary_array(data, aux, left, middle, right, counters):
    if data[middle] <= data[middle + 1]:
        return

    i, j, k = left, middle + 1, left

    while i <= middle and j <= right:
        counters["comparisons"] = counters["comparisons"] + 1
        if data[i] <= data[j]:
            aux[k] = data[i]
            i = i + 1
        else:
            aux[k] = data[j]
            j = j + 1
        counters["copies"] = counters["copies"] + 1
        k = k + 1

    while i <= middle:
        aux[k] = data[i]
        i = i + 1
        k = k + 1
        counters["copies"] = counters["copies"] + 1
    while j <= right:
        aux[k] = data[j]
        j = j + 1
        k = k + 1
        counters["copies"] = counters["copies"] + 1

    for i in range(left, right + 1):
        data[i] = aux[i]
        counters["copies"] = counters["copies"] + 1

def iterative_merge_sort_with_optimizations(data, cutoff=7):
    n = len(data)
    counters = {"comparisons": 0, "copies": 0}
    aux = data[:]
    start_time = time.time()

    for i in range(0, n, cutoff):
        cutoff_to_insertion(data, i, min(i + cutoff - 1, n - 1))

    size = cutoff
    while size < n:
        for left in range(0, n - size, size * 2):
            middle = left + size - 1
            right = min(left + size * 2 - 1, n - 1)
            eliminate_the_copy_to_the_auxiliary_array(data, aux, left, middle, right, counters)
        size = size * 2

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

merge_sort_data1, counters1 = iterative_merge_sort_with_optimizations(sorted_data)
merge_sort_data2, counters2 = iterative_merge_sort_with_optimizations(random_data)
merge_sort_data3, counters3 = iterative_merge_sort_with_optimizations(almost_sorted_data)
merge_sort_data4, counters4 = iterative_merge_sort_with_optimizations(reversed_data)
merge_sort_data5, counters5 = iterative_merge_sort_with_optimizations(few_unique_data)

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
#y1_1 = [0, 0, 0, 0, 0, 0]
#y1_2 = [0, 0, 0, 0, 0, 0]
#y1_3 = [0.0, 0.0, 0.0, 0.00998, 0.06, 0.735]
#y1_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y2_1 = [8, 377, 7404, 104221, 1359739, 17465820]
#y2_2 = [20, 796, 15364, 213680, 2771568, 35453404]
#y2_3 = [0.0, 0.0, 0.01, 0.12, 1.63, 22.475]
#y2_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y3_1 = [9, 180, 1586, 10238, 176309, 1572889]
#y3_2 = [20, 452, 4452, 27636, 452252, 4077584]
#y3_3 = [0.0, 0.0, 0.0, 0.00995, 0.27, 2.455]
#y3_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y4_1 = [3, 181, 3433, 50448, 677321, 8424605]
#y4_2 = [20, 796, 15364, 213680, 2771624, 35454048]
#y4_3 = [0.0, 0.0, 0.0096, 0.1099, 1.32, 16.72]
#y4_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y5_1 = [9, 351, 6957, 96132, 1243646, 15984258]
#y5_2 = [20, 796, 15364, 213652, 2771428, 35451500]
#y5_3 = [0.0, 0.0, 0.00995, 0.11, 1.425, 18.22]
#y5_4 = [344, 1872, 17176, 170176, 1700176, 17000176]