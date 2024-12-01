import time
import sys
from Laba6 import *

#1: Рекурсивний MergeSort
def top_down_merge_sort(data):
    counters = {"comparisons": 0, "copies": 0}

    def merge(left, right):
        nonlocal counters
        sorted_data = []
        i = j = 0
        while i < len(left) and j < len(right):
            counters["comparisons"] = counters["comparisons"] + 1
            if left[i] <= right[j]:
                sorted_data.append(left[i])
                i = i + 1
            else:
                sorted_data.append(right[j])
                j = j + 1
            counters["copies"] = counters["copies"] + 1
        sorted_data.extend(left[i:])
        sorted_data.extend(right[j:])
        counters["copies"] = counters["copies"] + len(left[i:]) + len(right[j:])
        return sorted_data

    def sort(data):
        if len(data) <= 1:
            return data
        middle = len(data) // 2
        left = sort(data[:middle])
        right = sort(data[middle:])
        return merge(left, right)

    start_time = time.time()
    merge_sort_data = sort(data)
    end_time = time.time()

    counters["time"] = end_time - start_time
    counters["memory"] = sys.getsizeof(data) + sys.getsizeof(merge_sort_data)
    return merge_sort_data, counters


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

merge_sort_data1, counters1 = top_down_merge_sort(sorted_data)
merge_sort_data2, counters2 = top_down_merge_sort(random_data)
merge_sort_data3, counters3 = top_down_merge_sort(almost_sorted_data)
merge_sort_data4, counters4 = top_down_merge_sort(reversed_data)
merge_sort_data5, counters5 = top_down_merge_sort(few_unique_data)

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
#y1_1 = [15, 316, 4932, 64608, 815024, 9884992]
#y1_2 = [34, 672, 9976, 133616, 1668928, 19951424]
#y1_3 = [0.0, 0.01, 0.0, 0.075, 0.95, 11.58]
#y1_4 = [400, 2016, 18224, 180224, 1800224, 18000224]

#y2_1 = [23, 530, 8687, 120483, 1536135, 18673840]
#y2_2 = [34, 672, 9976, 133616, 1668928, 19951424]
#y2_3 = [0.0, 0.0, 0.015, 0.14, 1.61, 20.9]
#y2_4 = [400, 1920, 18136, 177736, 1724576, 17697576]

#y3_1 = [18, 400, 5521, 71151, 863318, 10789240]
#y3_2 = [34, 672, 9976, 133616, 1668928, 19951424]
#y3_3 = [0.0, 0.0, 0.005, 0.09, 0.975, 12.38]
#y3_4 = [400, 2016, 18224, 177736, 1800224, 18000224]

#y4_1 = [19, 356, 5044, 69008, 853904, 10066432]
#y4_2 = [34, 672, 9976, 133616, 1668928, 19951424]
#y4_3 = [0.0, 0.0, 0.01, 0.075, 0.97, 11.57]
#y4_4 = [400, 2016, 18224, 180224, 1800224, 18000224]

#y5_1 = [24, 516, 8182, 111380, 1413460, 17128905]
#y5_2 = [34, 672, 9976, 133616, 1668928, 19951424]
#y5_3 = [0.0, 0.0, 0.009, 0.13, 1.49, 18]
#y5_4 = [400, 1920, 18224, 180224, 1800224, 18000224]
