import sys
sys.stdin = open('input.txt')
from pprint import pprint

def run(a, b):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    q = []
    q.append([a,b])
    visited[a][b] = 1
    while q:
        now = q.pop(0)
        for i in range(4):
            nr, nc = now[0] + dr[i], now[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[a][b]:
                if maze[nr][nc]:
                    q.append([nr, nc])
                    visited[nr][nc] = visited[now[0]][now[1]] + 1
                if nr == N - 1 and nc == M - 1:
                    return visited[nr][nc]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
run(0, 0)
print(visited[N-1][M-1])