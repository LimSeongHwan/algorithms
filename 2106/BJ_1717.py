import sys
sys.setrecursionlimit(50003)


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    node1_parent = find(node1)
    node2_parent = find(node2)

    if node1_parent > node2_parent:
        parent[node1_parent] = node2_parent
    else:
        parent[node2_parent] = node1_parent


n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    do, input1, input2 = map(int, sys.stdin.readline().split())

    if not do:
        union(input1, input2)
    else:
        if find(input1) == find(input2):
            print('YES')
        else:
            print("NO")