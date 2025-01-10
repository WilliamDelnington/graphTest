import pandas, collections
from DisjointSet import Graph, kruskalMST, dijkstra

dt = pandas.read_csv("dataset.txt", sep="\t+", header=None, engine="python")

dt.columns = ["Origin", "Destination", "Distance"]

df = pandas.DataFrame(dt)

# The nodes of the graphs obtained from the dataset.
s = set(dt["Origin"].iloc[i].strip() for i in range(dt["Origin"].count())).union(
    set(dt["Destination"].iloc[i].strip() for i in range(dt["Destination"].count()))
    )

# Sort the edges of the graphs by their distance.
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

test_cases = [
    ("Buon Ma Thuot", "Vinh"),
    ("Ha Noi", "Ho Chi Minh City"),
    ("Lao Cai", "Ha Noi"),
    ("Hai Phong", "Sapa"),
    ("Hoi An", "Ho Chi Minh City")
]

def main(source, destination):
    print(f"Getting the path from {source} to {destination}:")
    shortest_distance = dijkstra(graph, source, destination)
    print(f"The shortest distance from {source} to {destination} is {shortest_distance}")

for source, destination in test_cases:
    main(source, destination)