import sys
sys.stdin = open('input.txt')
from pprint import pprint

def bfs(x, y):
  queue = []
  queue.append([x, y])
  newone[x][y] = 1
  cnt = 1
  while queue:
    x, y = queue[0][0], queue[0][1]
    queue.pop(0)
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and newone[nx][ny] == 0:
        queue.append([nx, ny])
        newone[nx][ny] = 1
        cnt += 1

  return cnt

M, N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(K)]
newone = [[0]*N for _ in range(M)]
for i in range(K):
    for j in range(matrix[i][1], matrix[i][3]):
        for k in range(matrix[i][0], matrix[i][2]):
            newone[j][k] = 1

cntbox = 0
q = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# pprint(newone)
for i in range(M):
    for j in range(N):
        if newone[i][j] == 0:
            q.append(bfs(i, j))
            cntbox += 1
print(cntbox)
for i in sorted(q):
    print(i, end=' ')