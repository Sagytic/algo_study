import sys
sys.stdin = open('input.txt')
# 시간초과
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
def dfs(start, next, res, visited):
    global ans
    if len(visited) == N:
        if W[next][start] != 0:
            ans = min(ans, res + W[next][start])
        return
    for i in range(N):

        if start != i and W[next][i] != 0 and i not in visited:
            visited.append(i)
            dfs(start, i, res + W[next][i], visited)
            visited.pop()
for i in range(N):
    dfs(i, i, 0, [i])
print(ans)