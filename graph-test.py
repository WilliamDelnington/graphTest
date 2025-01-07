import pandas, collections
from DisjointSet import Graph, kruskalMST, dijkstra

dt = pandas.read_csv("dataset.txt", sep="\t+", header=None, engine="python")

dt.columns = ["Origin", "Destination", "Distance"]

df = pandas.DataFrame(dt)

s = set(dt["Origin"].iloc[i].strip() for i in range(dt["Origin"].count())).union(
    set(dt["Destination"].iloc[i].strip() for i in range(dt["Destination"].count()))
    )
edges = sorted(zip(
    [dt["Origin"].iloc[i].strip() for i in range(dt["Origin"].count())],
    [dt["Destination"].iloc[i].strip() for i in range(dt["Destination"].count())],
    [float(dt["Distance"].iloc[i]) for i in range(dt["Distance"].count())]
), key=lambda x: x[2])

mst_edges, cost = kruskalMST(s, edges)

graph = collections.defaultdict(list)
for u, v, weight in mst_edges:
    graph[u].append((v, weight))
    graph[v].append((u, weight))

source = "Buon Ma Thuot"
destination = "Vinh"
shortest_distance = dijkstra(graph, source, destination)
print(shortest_distance)