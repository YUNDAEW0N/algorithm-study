class Graph:
    def __init__(self, ver_count):
        self.ver_count = ver_count
        self.arr = [[0] * ver_count for _ in range(ver_count)]




def add_directed_edge(p, src, dest):
    p.arr[src][dest] = 1

def add_undirected_edge(p, src, dest):
    p.arr[src][dest] = 1
    p.arr[dest][src] = 1

def display(p):
    print("\n\n *** 간선 연결 현황 ***\n\n")
    for i in range(p.ver_count):
        print(f"출발지 {i} => {' '.join(map(str, p.arr[i]))}")

def memory_free(p):
    print("\n메모리 해제\n")
    p.arr = None

def main():
    grp = Graph(4)  # 정점의 개수

    add_undirected_edge(grp, 0, 1)  # 출발지, 도착지
    add_undirected_edge(grp, 0, 2)  # 출발지, 도착지
    add_undirected_edge(grp, 1, 2)  # 출발지, 도착지
    add_undirected_edge(grp, 2, 3)  # 출발지, 도착지

    display(grp)

    memory_free(grp)

if __name__ == "__main__":
    main()