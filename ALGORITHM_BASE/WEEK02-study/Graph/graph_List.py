#인접리스트 그래프 구현하기

class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class Graph:
    def __init__(self, count):
        self.vertex_count = count
        self.head = [None] * count

def graph_initialize(graph, count):
    graph.vertex_count = count
    graph.head = [Node(i) for i in range(count)]

def add_directed_edge(graph, src, dst):
    new_node = Node(dst)
    new_node.next = None

    if graph.head[src].next is None:
        graph.head[src].next = new_node
        return

    new_node.next = graph.head[src].next
    graph.head[src].next = new_node

def add_undirected_edge(graph, src, dst):
    add_directed_edge(graph, src, dst)
    add_directed_edge(graph, dst, src)

def display(graph):
    for i in range(graph.vertex_count):
        cur_node = graph.head[i].next
        print(f"출발지 노드 : {graph.head[i].vertex} => ", end="")

        while cur_node is not None:
            print(cur_node.vertex, end=" ")
            cur_node = cur_node.next

        print()

def memory_free(graph):
    for i in range(graph.vertex_count):
        while graph.head[i].next is not None:
            del_node = graph.head[i].next
            graph.head[i].next = del_node.next
            print(f"도착지 {del_node.vertex} 노드 제거")
            del del_node

    print("출발지 배열 제거")
    graph.head = None

def main():
    grp = Graph(4)  # 정점의 개수

    graph_initialize(grp, 4)

    add_undirected_edge(grp, 0, 1)
    add_undirected_edge(grp, 0, 2)
    add_undirected_edge(grp, 1, 2)
    add_undirected_edge(grp, 2, 3)

    display(grp)

    memory_free(grp)

if __name__ == "__main__":
    main()
