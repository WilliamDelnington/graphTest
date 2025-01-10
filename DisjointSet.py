class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, origin, destination, distance):
        self.graph.append([origin, destination, distance])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])

        return parent[i]
    
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        else:
            parent[y] = x
            rank[x] += 1

    def kruskalMST(self):
        result = []
        # Use for sorted edges
        i = 0

        # Uses for result[]
        e = 0

        # Sort the edge by non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            origin, destination, distance = self.graph[i]
            i = i + 1
            x = self.find(parent, origin)
            y = self.find(parent, destination)

            if x != y:
                e = e + 1
                result.append([origin, destination, distance])
                self.union(parent, rank, x, y)

        minimumCost = 0
        for origin, destination, distance in result:
            minimumCost += distance
            print("%d-->%d: %d" % (origin, destination, distance))
        print("Mininum distance:", minimumCost)

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskalMST(vertices, edges):
    # vertices = set(df["Origin"]).union(set(df["Destination"]))
    # edges = sorted(zip(df["Origin"], df["Destination"], df["Distance"]), key=lambda x: x[2])

    mst = []
    total_cost = 0

    ds = DisjointSet(vertices)

    for origin, destination, distance in edges:
        if ds.find(origin) != ds.find(destination):
            ds.union(origin, destination)
            mst.append((origin, destination, distance))
            total_cost += float(distance)

    return mst, total_cost

import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    distances = {v: float("inf") for v in graph}
    distances[start] = 0

    visited = set()

    while pq:
        curr_distance, curr_vertex = heapq.heappop(pq)
        if curr_vertex in visited:
            continue
        visited.add(curr_vertex)

        if curr_vertex == end:
            return curr_distance
        
        for neighbor, weight in graph[curr_vertex]:
            if neighbor not in visited:
                new_distance = curr_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

    return float("inf")