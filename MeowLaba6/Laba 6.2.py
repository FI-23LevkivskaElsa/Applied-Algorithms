import time
import sys
from Laba6 import *

#2: Ітеративний MergeSort
def bottom_up_merge_sort(data):
    counters = {"comparisons": 0, "copies": 0}

    n = len(data)
    width = 1
    start_time = time.time()
    temp = data[:]

    while width < n:
        for i in range(0, n, 2 * width):
            left = data[i:i + width]
            right = data[i + width:i + 2 * width]
            i_left, i_right = 0, 0
            merged = []
            while i_left < len(left) and i_right < len(right):
                counters["comparisons"] = counters["comparisons"] + 1
                if left[i_left] <= right[i_right]:
                    merged.append(left[i_left])
                    i_left = i_left + 1
                else:
                    merged.append(right[i_right])
                    i_right = i_right + 1
                counters["copies"] = counters["copies"] + 1
            merged.extend(left[i_left:])
            merged.extend(right[i_right:])
            counters["copies"] = counters["copies"] + len(left[i_left:]) + len(right[i_right:])
            data[i:i + len(merged)] = merged

        width = width * 2
    end_time = time.time()

    counters["time"] = end_time - start_time
    counters["memory"] = sys.getsizeof(data) + sys.getsizeof(temp)
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

merge_sort_data1, counters1 = bottom_up_merge_sort(sorted_data)
merge_sort_data2, counters2 = bottom_up_merge_sort(random_data)
merge_sort_data3, counters3 = bottom_up_merge_sort(almost_sorted_data)
merge_sort_data4, counters4 = bottom_up_merge_sort(reversed_data)
merge_sort_data5, counters5 = bottom_up_merge_sort(few_unique_data)

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
#y1_1 = [21, 372, 5052, 71712, 877968, 10095552]
#y1_2 = [40, 700, 10000, 140000, 1700000, 20000000]
#y1_3 = [0.0, 0.0, 0.008, 0.085, 0.99, 11.64]
#y1_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y2_1 = [26, 560, 8713, 123618, 1566360, 18715434]
#y2_2 = [40, 700, 10000, 140000, 1700000, 20000000]
#y2_3 = [0.0, 0.0, 0.015, 0.13, 1.66, 21.02]
#y2_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y3_1 = [22, 398, 5863, 81967, 886153, 10772234]
#y3_2 = [40, 700, 10000, 140000, 1700000, 20000000]
#y3_3 = [0.0, 0.0, 0.0064, 0.09, 1.01, 12.1]
#y3_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y4_1 = [15, 316, 4932, 64608, 815024, 9884992]
#y4_2 = [40, 700, 10000, 140000, 1700000, 20000000]
#y4_3 = [0.0, 0.0, 0.007, 0.075, 0.926, 11.33]
#y4_4 = [344, 1872, 17176, 170176, 1700176, 17000176]

#y5_1 = [26, 539, 8193, 115189, 1450605, 17208641]
#y5_2 = [40, 700, 10000, 140000, 1700000, 20000000]
#y5_3 = [0.0, 0.0, 0.0016, 0.13, 1.49, 17.9]
#y5_4 = [344, 1872, 17176, 170176, 1700176, 17000176]