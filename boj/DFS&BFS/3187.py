dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, s, w):
    global sheep, wolf
    q = []
    q.append([x, y])
    while q:
        new = q.pop(0)
        for i in range(4):
            nx, ny = new[0]+dx[i], new[1]+dy[i]
            if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] != '#':
                if matrix[nx][ny] == 'v':
                    matrix[nx][ny] = '#'
                    w += 1
                    q.append([nx, ny])
                elif matrix[nx][ny] == 'k':
                    matrix[nx][ny] = '#'
                    s += 1
                    q.append([nx, ny])
                elif matrix[nx][ny] == '.':
                    matrix[nx][ny] = '#'
                    q.append([nx, ny])
    if s > w:
        sheep += s
    else:
        wolf += w

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
sheep, wolf = 0, 0

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'v':
            matrix[i][j] = '#'
            dfs(i, j, 0, 1)
        elif matrix[i][j] == 'k':
            matrix[i][j] = '#'
            dfs(i, j, 1, 0)
print(sheep, wolf)