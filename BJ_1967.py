from heapq import heappush, heappop

def dijkstra(start):
    distance = [0xffffff] * (node_num + 1)                 ## 각 노드의 거리를 초기화
    q = []                                                 ## 최소힙 queue
    distance[start] = 0                                    ## 시작 노드의 거리는 0이다. 자기 자신으로 가는 거리는 0
    heappush(q, [0, start])                                ## 시작 노드를 힙에 넣어준다.

    while q:
        now_distance, now_node = heappop(q)                ## 최소 거리와, 최소 거리를 가진 노드를 가져온다.

        for node_distance, node in adj[now_node]:          ## 최소 거리를 가진 노드의 인접 노드와 인접 노드의 거리를 가져온다.
            sum_distance = now_distance + node_distance    ## 현재까지의 최소 거리와 인접 노드의 거리를 더해준다.

            if sum_distance < distance[node]:              ## 현재 가고자하는 인접노드의 거리와 시작 노드에서
                distance[node] = sum_distance              ## 해당 노드까지의 거리를 비교해준다.
                heappush(q, [sum_distance, node])          ## 시작 노드에서 해당 노드까지의 거리가 더 길 경우
                                                           ## 현재 진행 중인 경로가 최소 거리이기 때문에 갱신해준다.
    return distance                                        ## 해당 노드와 최소 거리 값을 최소 힙에 넣어준다.
                                                           ## 시작 노드로 부터 각 노드별 거리 값을 return
node_num = int(input())
adj = [[] for _ in range(node_num + 1)]
for _ in range(node_num - 1):
    parent, child, distance = map(int, input().split())
    adj[parent].append((distance, child))
    adj[child].append((distance, parent))

rootToleaf = dijkstra(1)                                        ## 1번 노드에서 각 노드까지의 거리가 rootToleaf에 들어간다.
half_max_distance_node = rootToleaf.index(max(rootToleaf[1:]))  ## max(rootToleaf[1:])가 가장 아래 레벨에 있는 노드인지는 알 수 없으나
max_distance = max(dijkstra(half_max_distance_node)[1:])        ## 1번 노드로부터 가장 긴 거리를 가진 노드인 것은 알 수 있다.
print(max_distance)                                             ## 즉 적어도 1번 노드의 자식 노드 중 한 노드의 최장 거리를 구한 것
                                                                ## 최장 거리를 가진 자식노드를 dijkstra에 넣어서 각 노드별 거리를 구한다.
                                                                ## 각 노드별 거리 중 가장 긴 거리는 
                                                                ## 1번 노드의 나머지 자식 노드의 최장 거리와 같게 되므로
                                                                ## 결과적으로 노드 사이에서 가장 긴 거리임을 보장한다.