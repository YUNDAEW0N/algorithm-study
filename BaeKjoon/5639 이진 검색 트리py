import sys

sys.setrecursionlimit(10**8)
pre = []
graph = []

while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break

def insert_node(current_root, value):
    if current_root is None:
        # 현재 노드가 None이면 새로운 노드를 만들어 반환
        return {'value': value, 'left': None, 'right': None}

    if value < current_root['value']:
        # 삽입할 값이 현재 노드의 값보다 작으면 왼쪽 서브트리로 이동
        current_root['left'] = insert_node(current_root['left'], value)
    else:
        # 삽입할 값이 현재 노드의 값보다 크거나 같으면 오른쪽 서브트리로 이동
        current_root['right'] = insert_node(current_root['right'], value)

    return current_root  # 현재 노드를 반환




def postorder(node):
    if node is not None:
        postorder(node['left'])
        postorder(node['right'])
        graph.append(node['value'])




root = None

for value in pre:
    root = insert_node(root, value)



postorder(root)
for i in range(len(graph)):
    print(graph[i])
