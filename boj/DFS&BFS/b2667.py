import sys
sys.stdin = open('input.txt')
from pprint import pprint

def bfs(x, y):
    vil = 1
    matrix[x][y] = 0
    queue = []
    queue.append([x, y])
    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 1 and not([nx,ny] in visited):
                matrix[nx][ny] = 0
                visited.append([nx, ny])
                vil += 1
                queue.append([nx, ny])
    return vil
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = []
box = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            box.append(bfs(i, j))
print(len(box))
for i in sorted(box):
    print(i)
