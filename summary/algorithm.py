#### 다익
"""
1. 기본 정보
0번 지점에서 V번 지점까지 이동하는데 걸리는 최소 거리 출력
방향 존재

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 시작(start)과 끝(end) 그리고 구간의 거리(w) 정보

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

다익스트라
 - 시작 지점으로부터 특정 지점까지의 최소 거리(비용)을 아는 것이 포인트
  - 어떤 정점을 거쳐왔는지 알 수 없음
 - prim과 비슷한 방식으로 구현
  - 다만, 최소 비용을 갱신 하는 과정에서 차이가 발생
 - 음수 가중치 허용하지 않음
"""

def dijkstra():
    for _ in range(V):
        min_idx = -1                                                        # 최소 인덱스 & 값 초기화
        min_value = 987654321
        for i in range(V+1):                                                # 최솟값 & 그때의 인덱스 찾기
            if not visited[i] and min_value > dist[i]:                      # 아직 i정점에 방문하지 않았고 dist[i]가 최솟값보다 작은 경우
                min_idx = i                                                 # 최솟값 인덱스 갱신
                min_value = dist[i]                                         # 최솟값 갱신
        visited[min_idx] = 1                                                # 최종 최솟값 갱신 후 방문처리

        for j in range(V+1):                                                # 인접 행렬에서 min_idx의 인접인 정점 중에서 최소 거리 갱신
            """
            A -> E        dist[j]
            A -> B -> E   dist[min_idx] + G[min_idx][j]
            """
            if not visited[j] and dist[j] > dist[min_idx] + G[min_idx][j]:  # 만약 j번 째를 방문하지 않았고
                                                                            # 바로 가려는 값(dist[j])이 거쳐가는 값(dist[min_idx] + G[min_idx][j])보다 더 크다면 == 더 짧은 거리로 이동 가능하다면
                dist[j] = dist[min_idx] + G[min_idx][j]                     # 그 값을 최소 거리로 갱신
    return dist[V]                                                          # 마지막 V번 지점까지의 거리

import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())                               # V: 마지막 노드 번호(0~V) / E: 간선
G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]      # 가중치 초기화 (최소 거리를 구해야 하기 때문에 가중치로 사용하지 않는 큰 값으로 초기화)
dist = [987654321] * (V+1)                                     # 비용(거리) 초기화
dist[0] = 0                                                    # 시작 정점 지점 (0번 -> 0번의 거리는 0)
visited = [0] * (V+1)                                          # 방문 체크
for _ in range(E):
    start, end, w = map(int, input().split())                  # 유향(방향있는) 그래프
    G[start][end] = w                                          # 시작 / 끝 / 가중치(길이)
print(dijkstra())                                              # 10

# 상호배타집합
def make_set(x):
    p[x] = x

def find_set(x):
    # 반복 구조
    while x != p[x]:
        x = p[x]
    return x

    # 재귀 구조
    # if p[x] != x:
    #     p[x] = find_set(p[x])
    # return p[x]

def union(x, y):
    # x, y = find_set(x), find_set(y)
    p[find_set(y)] = find_set(x)

# 1.
p = [0] * (6 + 1)
for i in range(7):
    make_set(i)

# p = list(range(7))
print(p)
print('----------------------------------')

# 2.
union(1, 3)
print(p)
print('----------------------------------')

union(2, 3)
print(p)
print('----------------------------------')

union(5, 6)
print(p)
print('----------------------------------')

# 3.
print(find_set(6))
print(find_set(3))
print(find_set(2))

# 크루스칼
"""
1. 기본 정보
MST의 최솟값의 합 구하기

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드(start, end)와 가중치(w)

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

크루스칼
 - 간선 중심
 - 간선을 오름차순 정렬 & 간선 개수만큼 선택
 - union & find 활용하여 사이클이 만들어 지는 것을 방지
"""

def make_set(x):
    """
    유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
    """
    p[x] = x                     # 노드 x의 부모 저장

def find_set(x):
    """
    x를 포함하는 집합을 찾는 연산
    """
    if p[x] != x:                # x가 루트가 아닌 경우
        p[x] = find_set(p[x])    # 다시 루트 찾아서 재귀 호출
    return p[x]                  # x의 대표값 반환

def union(x, y):
    """
    x와 y를 포함하는 두 집합을 통합하는 연산
    """
    p[find_set(y)] = find_set(x) # y의 대표자를 x의 대표자로 변경


def kruskal():
    global ans
    edge_cnt = idx = 0                       # ans(최종 가중치 누적값) / edge_cnt(간선 선택 개수 -> V개 선택) / idx (간선 정보를 컨트롤을 위한 제어 변수)

    while edge_cnt != V:                     # 선택한 간선의 수(edge_cnt)가 전체 정점의 수(V)와 같아지기 전까지(신장 트리 조건)
        x = edges[idx][0]                    # 간선 정보에서 두 정점을 찾아
        y = edges[idx][1]
                                             # 두 점의 대표 원소 비교 (대표 원소가 다르면 같은 집합 아니고 같으면 같은 집합이기 때문에 사이클 형성)
        if find_set(x) != find_set(y):       # 같은 그룹이 아닐 때만 (사이클 방지)
            union(x, y)                      # union
            edge_cnt += 1                    # union을 한 것은 간선을 선택 한 것을 의미하니 edge_cnt를 증가
            ans += edges[idx][2]             # 해당 간선의 가중치를 누적하자
        idx += 1                             # 위의 조건문에 관계없이 다음 간선을 선택하기 위해 idx를 증가
                                             # 사이클이 생겨 뛰어넘는 경우 if 조건문을 타지 않으니 다음 간선 선택을 위해 idx는 어떤 경우에도 증가 필요

import sys
sys.stdin = open('input.txt')
ans = 0
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]  # 간선 정보
p = [0] * (V+1)                                              # 상호배타집합에 활용 할 노드 정보 (인덱스를 맞춰주기 위해 V+1)
edges = sorted(edges, key=lambda x: x[2])                    # 가중치(인덱스 2번)를 기준으로 정렬

# p = list(range(V+1))
for i in range(V+1):
    make_set(i)
kruskal()
print(ans)                                                   # 22

# 프림
"""
1. 기본 정보
MST의 최솟값의 합 구하기

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드(start, end)와 가중치(w)

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

프림
 - 정점 중심 (임의의 정점을 잡고 시작)
 - 정점과 인접하는 정점 중에서 최소 비용의 간선이 존재하는 정점 선택
 - 계속 가중치가 최소인 정점을 연결해가며 최종적으로 연결된 배열의 합
"""

def prim():
    for _ in range(V):                                     # 모든 정점이 MST에 포함될 때까지 반복
        min_idx = -1
        min_value = 987654321
                                                           # key가 최솟값을 갖는 인덱스 찾기
        for i in range(V+1):                               # 인접 행렬이기 때문에 전체를 돌면서 확인
            if not visited[i] and key[i] < min_value:      # i번째 정점을 선택하지 않았고 선택하지 않은 정점 중에서 가장 적은 값이라면
                min_idx = i                                # 최솟값 인덱스 초기화
                min_value = key[i]                         # 최솟값 초기화
        visited[min_idx] = 1                               # 해당 정점 사용 처리

        for i in range(V+1):                               # min_idx와 연결된 인접 행렬 돌면서
            if not visited[i] and G[min_idx][i] < key[i]:  # 정점 선택 안했고 해당 가중치가 key의 요소보다 작으면 (== 더 적은 비용으로 MST에 연결되면)
                key[i] = G[min_idx][i]                     # 가중치 갱신

    return sum(key)                                        # 최종 간선의 가중치

import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())                                # V개의 정점 -> 0부터 시작하기 때문에 개수는 +1
G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]       # 임의의 큰 값으로 초기화
key = [987654321] * (V+1)                                       # 갱신된 최솟값 가중치(처음은 임의의 큰 값으로 초기화) -> MST에 속하는데 포함되는 비용(가중치)
key[0] = 0                                                      # 0번 정점을 시작 정점으로 선택 (처음은 가중치가 0)
visited = [0] * (V+1)                                           # 현재 정점을 선택했는지 여부 체크 (MST에 속하는지 여부)
for i in range(E):
    start, end, W = map(int, input().split())                   # start, end, W: 가중치
    G[start][end] = W                                           # 무향 그래프이므로 양쪽에 모두 가중치 체크
    G[end][start] = W

print(prim())                                                   # 22