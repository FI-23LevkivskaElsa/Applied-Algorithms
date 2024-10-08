import random

class SparseSet:
    def __init__(self, maxVal, capacity):
        self.sparse = [0] * (maxVal + 1)
        self.dense = [0] * capacity
        self.capacity = capacity
        self.maxVal = maxVal
        self.n = 0

    def insert(self, x):
        if x > self.maxVal:
            return print("Помилка! Значення елемента перевищує заданого значення.")
        if self.n >= self.capacity:
            return print("Помилка! Розмір множини перевищує заданий розмір.")
        if self.search(x) == -1:
            self.dense[self.n] = x
            self.sparse[x] = self.n
            self.n += 1

    def delete(self, x):
        if self.search(x) == -1:
            return print("Помилка! Не можна видалити елемент, якого немає в множині.")
        tmp = self.dense[self.n - 1]
        self.dense[self.sparse[x]] = tmp
        self.sparse[tmp] = self.sparse[x]
        self.n -= 1
        return print("Елемент", x, "видалено!")

    def search(self, x):
        if x > self.maxVal:
            return -1
        if self.sparse[x] < self.n and self.dense[self.sparse[x]] == x:
            return self.sparse[x]
        return -1

    def clear(self):
        self.n = 0
        return print("Множину повністю очищено!")

    def union(self, set2):
        UnionCapacity = self.n + set2.n
        UnionMaxVal = max(self.maxVal, set2.maxVal)
        UnionSet = SparseSet(UnionMaxVal, UnionCapacity)
        for i in range(self.n):
            UnionSet.insert(self.dense[i])
        for i in range(set2.n):
            UnionSet.insert(set2.dense[i])
        return UnionSet

    def intersection(self, set2):
        IntersectionCapacity = min(self.n, set2.n)
        IntersectionMaxVal = max(set2.maxVal, self.maxVal)
        IntersectionSet = SparseSet(IntersectionMaxVal, IntersectionCapacity)
        for i in range(self.n):
            if set2.search(self.dense[i]) != -1:
                IntersectionSet.insert(self.dense[i])
        return IntersectionSet

    def set_difference(self, set2):
        SetDifferenceCapacity = max(self.n, set2.n)
        SetDifferenceMaxVal = max(set2.maxVal, self.maxVal)
        SetDifferenceSet = SparseSet(SetDifferenceMaxVal, SetDifferenceCapacity)
        for i in range(self.n):
            if set2.search(self.dense[i]) == -1:
                SetDifferenceSet.insert(self.dense[i])
        return SetDifferenceSet

    def sym_difference(self, set2):
        SymDifferenceCapacity = self.n + set2.n
        SymDifferenceMaxVal = max(set2.maxVal, self.maxVal)
        SymDifferenceSet = SparseSet(SymDifferenceMaxVal, SymDifferenceCapacity)
        for i in range(self.n):
            if set2.search(self.dense[i]) == -1:
                SymDifferenceSet.insert(self.dense[i])
        for i in range(set2.n):
            if self.search(set2.dense[i]) == -1:
                SymDifferenceSet.insert(set2.dense[i])
        return SymDifferenceSet

    def is_subset(self, set1):
        for i in range(self.n):
            if set1.search(self.dense[i]) == -1:
                return print("Множина В НЕ Є підмножиною А.")
        return print("Множина В Є підмножиною А.")

    def print(self):
        for i in range(self.n):
            print(self.dense[i], end=' ')
        print()

#перевірка операцій insert, delete, search, clear
"""Set = SparseSet(65536, 65536)
for x in random.sample(range(1, 10), 7):
    Set.insert(x)
print("Множина А:")
Set.print()

Set.delete(5)
print("Множина А:")
Set.print()

Search = Set.search(3)
if Search == -1:
    print("Елемента 3 немає в множині.")
else:
    print("Елемент 3 є в множині.")

Set.clear()
print("Множина А:")
Set.print()"""

#перевірка операцій union, intersection, set difference, sym difference, is_subset
"""Set1 = SparseSet(65536, 65536)
for x in random.sample(range(1, 8), 7):
    Set1.insert(x)
print("Множина А:")
Set1.print()
Set2 = SparseSet(65536, 65536)
for y in random.sample(range(4, 10), 6):
    Set2.insert(y)
print("Множина В:")
Set2.print()

Set3 = Set1.union(Set2)
print("Об'єднання множин А і В:")
Set3.print()
Set4 = Set1.intersection(Set2)
print("Перетин мнoжин А і В:")
Set4.print()
Set5 = Set1.set_difference(Set2)
print("Різниця множин А\В:")
Set5.print()
Set6 = Set1.sym_difference(Set2)
print("Симетрична різниця множин А і В:")
Set6.print()
IsSubset = Set2.is_subset(Set1)"""

#знаходження даних для експериментів
"""Set = SparseSet(65536, 65536)
for x in random.sample(range(1, 65536), 65000):
    Set.insert(x)
TimeSearch = timeit.timeit('Set.search(5000)', globals=globals(), number=1000)
print(f"Час виконання операції пошуку: {TimeSearch} секунд для 1000 пошуків")"""

"""Set1 = SparseSet(65536, 65536)
for x in random.sample(range(1, 65536), 65000):
    Set1.insert(x)
Set2 = SparseSet(65536, 65536)
for y in random.sample(range(1, 65536), 65000):
    Set2.insert(y)
TimeUnion = timeit.timeit('Set1.union(Set2)', globals=globals(), number=100)
print(f"Час виконання об'єднання : {TimeUnion} секунд для 100 об'єднань")"""

#побудова графіків
"""x = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000]
y1 = [0.47*10**(-6), 0.442*10**(-6), 0.475*10**(-6), 0.453*10**(-6), 0.446*10**(-6), 0.45*10**(-6), 0.48*10**(-6), 0.47*10**(-6), 0.475*10**(-6), 0.45*10**(-6), 0.44*10**(-6), 0.45*10**(-6), 0.46*10**(-6), 0.459*10**(-6)]
y2 = [0.485*10**(-6), 0.5*10**(-6), 0.51*10**(-6), 0.487*10**(-6), 0.508*10**(-6), 0.52*10**(-6), 0.5*10**(-6), 0.52*10**(-6), 0.51*10**(-6), 0.5*10**(-6), 0.5*10**(-6), 0.517*10**(-6), 0.5*10**(-6), 0.5*10**(-6)]
y3 = [0.003, 0.014, 0.032, 0.047, 0.065, 0.079, 0.097, 0.115, 0.138, 0.147, 0.17, 0.175, 0.206, 0.212]

plt.plot(x, y3, label='Квадрати')
plt.title('Операція Union')
plt.xlabel('Розмір множин')
plt.ylabel('Час виконання операції')
plt.show()"""
