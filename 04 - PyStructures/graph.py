from networkx import Graph, shortest_path

graph = Graph()
graph.add_edge("Alice", "Bob", weight=1)
graph.add_edge("Bob", "Diana", weight=2)
graph.add_edge("Alice", "Diana", weight=4)

# Find the shortest path
shortest_path = shortest_path(graph, source="Alice", target="Diana", weight="weight")
print(f"Shortest path from Alice to Diana: {shortest_path}")
