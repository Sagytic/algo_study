import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque

def short_node():       # 가장 가까운 노드 반환
    val = INF
    idx = 0
    for i in range(1, N+1):
        if distance[i] > val and not visited[i]:
            val = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0     # 시작점은 0으로 초기화
    visited[start] = 1      # 방문
    for i in Wadj[start]:   # 최단거리 갱신
        distance[i[0]] = i[1]
    for i in range(N-1):    # 노드 반복
        now = short_node()  # 가장 가까운노드 방문처리
        visited[now] = 1
        for j in Wadj[now]: # 현재 + 다음노드 가는 비용 계싼
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:   # 갱신
                distance[j[0]] = cost
    return

for tc in range(1, int(input())+1):
    ans = 0
    INF = 987654321
    N, E = map(int, input().split())        # N: 도착점 / E: 간선 수
    visited = [0]*(N+1)                     # 방문체크
    distance = [-INF]*(N+1)                  # 최단거리 계산
    adj = [list(map(int, input().split())) for _ in range(E)]
    Wadj = [[] for i in range(N+1)]          # 경로 / 0번노드부터 / N번까지

    for i in range(E):
        a, b, c = adj[i][0], adj[i][1], -adj[i][2]
        Wadj[a].append((b, c))

    # pprint(Wadj)
    # # pprint(Wmat)
    # pprint(mat)
    dijkstra(0)         # 0번노드 출발
    ans = distance[N]   # N번 노드 값 반환
    print(distance)
    print('#{} {}'.format(tc, ans))
