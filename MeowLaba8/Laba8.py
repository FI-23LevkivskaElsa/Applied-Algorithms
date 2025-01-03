import numpy as np
import random
import time
import sys
import matplotlib as plt

from queue import PriorityQueue

priority_queue = PriorityQueue()
priority_queue.put((1, "A"))
priority_queue.put((3, "B"))
priority_queue.put((2, "C"))
priority_queue.put((5, "D"))
priority_queue.put((4, "E"))
print("Розмір створеної черги дорівнює:", priority_queue.qsize())

while not priority_queue.empty():
    print(priority_queue.get())

print("Розмір черги дорівнює:", priority_queue.qsize())


class Stats:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.memory = 0

    def record_memory(self, obj):
        self.memory = self.memory + sys.getsizeof(obj)


def heapify(arr, n, i, stats):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        stats.comparisons = stats.comparisons + 1
        largest = left

    if right < n and arr[largest] < arr[right]:
        stats.comparisons = stats.comparisons + 1
        largest = right

    if largest != i:
        stats.swaps = stats.swaps + 1
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest, stats)


def heap_sort(arr):
    stats = Stats()
    stats.record_memory(arr)
    n = len(arr)

    if n <= 1:
        return arr

    for i in range((n - 1) // 2, -1, -1):
        heapify(arr, n, i, stats)

    for i in range(n - 1, 0, -1):
        stats.swaps = stats.swaps + 1
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, stats)

    stats.record_memory(arr)
    return arr, stats


def generate_data(data, size):
    if data == "same":
        return [69] * size

    elif data == "sorted":
        return list(range(size))

    elif data == "random":
        return [random.randint(0, 1000000) for _ in range(size)]

    elif data == "nearly_sorted":
        arr = list(range(size))
        swaps = max(1, size // 10)
        for _ in range(swaps):
            i, j = random.sample(range(size), 2)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    elif data == "reversed":
        return list(range(size, 0, -1))

    elif data == "triangular":
        half = size // 2
        first_half = list(range(half))
        return first_half + first_half[::-1]

    elif data == "few_unique":
        return list(np.random.choice(range(5), size))


def run_heapsort(size, data):
    arr = generate_data(data, size)
    start_time = time.time()
    _, stats = heap_sort(arr)
    finish_time = time.time() - start_time
    return finish_time, stats


size = 100
x = [1000000, 100000, 10000, 1000, 100]

timer1, counter1 = run_heapsort(size, "same")
print(f"HeapSort, де на вхід подається набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
y1_t = [1.331997, 0.136001, 0.014, 0.002, 0]
y1_c = [0, 0, 0, 0, 0]
y1_s = [999999, 99999, 9999, 999, 99]
y1_m = [16000128, 1600128, 160128, 16128, 1728]

timer2, counter2 = run_heapsort(size, "sorted")
print(f"HeapSort, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
y2_t = [26.829011, 2.216012, 0.175021, 0.013, 0.000999]
y2_c = [28090484, 2303177, 180584, 12963, 795]
y2_s = [19787792, 1650854, 131956, 9708, 640]
y2_m = [18000224, 1800224, 180224, 18224, 2016]

timer3, counter3 = run_heapsort(size, "random")
print(f"HeapSort, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
y3_t = [31.554003, 2.392997, 0.174, 0.013, 0.001002]
y3_c = [26622260, 2163377, 166371, 11732, 671]
y3_s = [19049373, 1575014, 124142, 9115, 572]
y3_m = [17394928, 1648928, 175248, 18048, 1824]

timer4, counter4 = run_heapsort(size, "nearly_sorted")
print(f"HeapSort, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
y4_t = [27.933024, 2.261998, 0.171, 0.01202, 0]
y4_c = [27778765, 2274458, 176882, 12686, 751]
y4_s = [19647870, 1635812, 130064, 9578, 626]
y4_m = [18000224, 1800224, 180224, 18224, 2016]

timer5, counter5 = run_heapsort(size, "reversed")
print(f"HeapSort, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
y5_t = [24.72117, 1.998985, 0.154014, 0.010979, 0]
y5_c = [25233624, 2024810, 153619, 10340, 561]
y5_s = [18333408, 1497434, 116696, 8316, 516]
y5_m = [18000224, 1800224, 180224, 18224, 2016]

timer6, counter6 = run_heapsort(size, "triangular")
print(f"HeapSort, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
y6_t = [26.619989, 2.165963, 0.166986, 0.012021, 0.000999]
y6_c = [26676227, 2163739, 168257, 11781, 684]
y6_s = [19225332, 1585853, 125173, 9235, 589]
y6_m = [16000128, 1600128, 160128, 16128, 1728]

timer7, counter7 = run_heapsort(size, "few_unique")
print(f"HeapSort, де на вхід подаються дані з кількома унікальними значеннями:")
print(f"Time: {timer7:.6f}s, Comparisons: {counter7.comparisons}, Swaps: {counter7.swaps}, Memory: {counter7.memory}")
y7_t = [21.033012, 1.716035, 0.136, 0.01, 0.001001]
y7_c = [18602130, 1518001, 117848, 8353, 487]
y7_s = [15063180, 1252113, 100330, 7320, 486]
y7_m = [18000224, 1800224, 180224, 18224, 2016]


"""plt.plot(x, y1_t, color='red', label='Однаковий набір елементів')
plt.plot(x, y2_t, color='orange', label='Відсортовані дані')
plt.plot(x, y3_t, color='yellow', label='Випадкові дані')
plt.plot(x, y4_t, color='green', label='Майже відсортовані дані')
plt.plot(x, y5_t, color='blue', label='Відсортовані в зворотному порядку дані')
plt.plot(x, y6_t, color='purple', label='"Трикутні" дані')
plt.plot(x, y7_t, color='pink', label='Дані з кількома унікальними значеннями')
plt.title("Час виконання HeapSort")
plt.xlabel('Розмір вхідних даних')
plt.ylabel("Час виконання")
plt.legend()
plt.show()"""

"""plt.plot(x, y1_c, color='red', label='Однаковий набір елементів')
plt.plot(x, y2_c, color='orange', label='Відсортовані дані')
plt.plot(x, y3_c, color='yellow', label='Випадкові дані')
plt.plot(x, y4_c, color='green', label='Майже відсортовані дані')
plt.plot(x, y5_c, color='blue', label='Відсортовані в зворотному порядку дані')
plt.plot(x, y6_c, color='purple', label='"Трикутні" дані')
plt.plot(x, y7_c, color='pink', label='Дані з кількома унікальними значеннями')
plt.title("Кількість порівнянь під час HeapSort")
plt.xlabel('Розмір вхідних даних')
plt.ylabel("Кількість порівнянь")
plt.legend()
plt.show()"""

"""plt.plot(x, y1_s, color='red', label='Однаковий набір елементів')
plt.plot(x, y2_s, color='orange', label='Відсортовані дані')
plt.plot(x, y3_s, color='yellow', label='Випадкові дані')
plt.plot(x, y4_s, color='green', label='Майже відсортовані дані')
plt.plot(x, y5_s, color='blue', label='Відсортовані в зворотному порядку дані')
plt.plot(x, y6_s, color='purple', label='"Трикутні" дані')
plt.plot(x, y7_s, color='pink', label='Дані з кількома унікальними значеннями')
plt.title("Кількість обмінів під час HeapSort")
plt.xlabel('Розмір вхідних даних')
plt.ylabel("Кількість обмінів")
plt.legend()
plt.show()"""

"""plt.plot(x, y1_m, color='red', label='Однаковий набір елементів')
plt.plot(x, y2_m, color='orange', label='Відсортовані дані')
plt.plot(x, y3_m, color='yellow', label='Випадкові дані')
plt.plot(x, y4_m, color='green', label='Майже відсортовані дані')
plt.plot(x, y5_m, color='blue', label='Відсортовані в зворотному порядку дані')
plt.plot(x, y6_m, color='purple', label='"Трикутні" дані')
plt.plot(x, y7_m, color='pink', label='Дані з кількома унікальними значеннями')
plt.title("Кількість використаної пам'яті під час HeapSort")
plt.xlabel('Розмір вхідних даних')
plt.ylabel("Кількість пам'яті")
plt.legend()
plt.show()"""
