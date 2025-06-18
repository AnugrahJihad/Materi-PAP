graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Tambah simpul
def add_node(node):
    if node not in graph:
        graph[node] = []

# Tambah sisi
def add_edge(node1, node2):
    if node1 in graph and node2 in graph:
        graph[node1].append(node2)
        graph[node2].append(node1)  # untuk graph tak berarah

# Tampilkan graph
def display_graph():
    for node in graph:
        print(f"{node} -> {graph[node]}")
