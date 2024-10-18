import random
import timeit
import pandas as pd
import matplotlib.pyplot as plt

class DirectedGraph():
    def __init__(self, n):
        self.n = n
        self.list = {i: [] for i in range(1, n + 1)}

    def add_vert(self):
        self.list[self.n] = []
        self.n = self.n + 1

    def del_vert(self, v):
        if v in self.list:
            self.list.pop(v)
            for begin, end in self.list.items():
                if v in end:
                    end.remove(v)

    def add_edge(self, v, u):
        if u not in self.list[v]:
            self.list[v].append(u)

    def del_edge(self, v, u):
        if u in self.list[v]:
            self.list[v].remove(u)

    def listTOmatrix(self):
        matrix = [[0] * self.n for _ in range(self.n)]
        for v in self.list:
            for u in self.list[v]:
                matrix[v - 1][u - 1] = 1
        return matrix

    def ErdosRenyi_model(self, p: float):
        for v in self.list:
            for u in self.list:
                if random.random() <= p:
                    self.add_edge(v, u)

    def print_graph(self):
        for begin, end in self.list.items():
            print(begin, ":", end)

"""G = DirectedGraph(5)
G.add_edge(1, 2)
G.add_edge(2, 5)
G.add_edge(5, 4)
G.add_edge(4, 3)
#G.add_edge(3, 1)
G = G.listTOmatrix()
for row in G:
    print(row)"""


def recursive_dfs(graph, v, visited):
    n = len(graph)
    visited[v] = True
    for i in range(n):
        if graph[v][i] == 1 and visited[i] == False:
            recursive_dfs(graph, i, visited)
    return visited

"""is_graph_connected_by_DFS = recursive_dfs(G, 1, [False] * len(G))
print(is_graph_connected_by_DFS)"""


def WarshallAlgorithm(graph):
    n = len(graph)
    W = [graph for _ in range(n+1)]
    W[0] = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[k][i][j] = W[k-1][i][j] or (W[k-1][i][k] and W[k-1][k][j])
    return W[n]

"""is_graph_connected_by_Warshall = WarshallAlgorithm(G)
for row in is_graph_connected_by_Warshall:
    print(row)"""



"""Graph = DirectedGraph(100)
Graph.ErdosRenyi_model(1)
Graph = Graph.listTOmatrix()

n = len(Graph)
visited = [False] * n
TimeDFS = timeit.timeit('recursive_dfs(Graph, 1, visited)', globals=globals(), number=100)
print(f"Час виконання операції : {TimeDFS} секунд для 100 операцій")

TimeWarshall = timeit.timeit('WarshallAlgorithm(Graph)', globals=globals(), number=100)
print(f"Час виконання операції : {TimeWarshall} секунд для 100 операцій")"""



"""pd.set_option('display.max_columns', None)
df_DFS = pd.read_csv('DFS.csv')
print(df_DFS.head(), '\n ')

df_Warshall = pd.read_csv('Warshall.csv')
print(df_Warshall.head())"""

"""X = df_DFS[['num_vert']]
y1 = df_DFS['p_10']
y2 = df_DFS['p_25']
y3 = df_DFS['p_50']
y4 = df_DFS['p_75']
y5 = df_DFS['p_100']
plt.plot(X, y1, color='red', label='Щільність 10%')
plt.plot(X, y2, color='orange', label='Щільність 25%')
plt.plot(X, y3, color='green', label='Щільність 50%')
plt.plot(X, y4, color='blue', label='Щільність 75%')
plt.plot(X, y5, color='purple', label='Щільність 100%')
plt.title("Час виконання перевірки зв'язності графа за допомогою DFS")
plt.xlabel('Кількість вершин в графі')
plt.ylabel("Час виконання")
plt.legend()"""

"""X = df_Warshall[['num_vert']]
y1 = df_Warshall['p_10']
y2 = df_Warshall['p_25']
y3 = df_Warshall['p_50']
y4 = df_Warshall['p_75']
y5 = df_Warshall['p_100']
plt.plot(X, y1, color='red', label='Щільність 10%')
plt.plot(X, y2, color='orange', label='Щільність 25%')
plt.plot(X, y3, color='green', label='Щільність 50%')
plt.plot(X, y4, color='blue', label='Щільність 75%')
plt.plot(X, y5, color='purple', label='Щільність 100%')
plt.title("Час виконання перевірки зв'язності графа за допомогою алгоритму Уоршелла")
plt.xlabel('Кількість вершин в графі')
plt.ylabel("Час виконання")
plt.legend()
plt.show()"""

