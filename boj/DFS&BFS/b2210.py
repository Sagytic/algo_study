import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y, ans):
    global anslist
    if len(ans) == 6:
        if ans not in anslist:
            anslist.append(ans)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, ans+matrix[nx][ny])

matrix = [input().split() for _ in range(5)]
anslist = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])
print(len(anslist))