def topologicalSortUtil(node, graph, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            topologicalSortUtil(neighbor, graph, visited, stack)
    stack.insert(0, node)

def topologicalSort(graph):
    visited = {node: False for node in graph}
    stack = []
    for node in graph:
        if not visited[node]:
            topologicalSortUtil(node, graph, visited, stack)
    return stack

# Example usage:
if __name__ == "__main__":
    # Graph representing course prerequisites
    graph = {
        'Algoritma dan Struktur Data': ['Pemrograman Dasar'],
        'Pemrograman Dasar': ['Pengantar Informatika'],
        'Pengantar Informatika': [],
        'Matematika Diskrit': ['Pemrograman Dasar'],
        'Sistem Operasi': ['Algoritma dan Struktur Data', 'Matematika Diskrit'],
        'Jaringan Komputer': ['Sistem Operasi']
    }
    print("Topological order for course registration:", topologicalSort(graph))
