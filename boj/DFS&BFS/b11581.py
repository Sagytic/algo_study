def bfs(n):
    global ans, flag
    tmp = crossline[n]
    for i in tmp:
        if i == N:
            return
        if visited[i] == 1:
            ans = 'CYCLE'
            flag = True
            return
        elif visited[i] == 0:
            visited[i] += 1
        if flag:
            return
        bfs(i)
        visited[i] = 0

N = int(input())
visited = [0] + [0]*N
visited[1] = 1
ans = 'NO CYCLE'
flag = False
line = [list(map(int, input().split())) for _ in range((N-1)*2)]
crossline = {}
a = 0
for li in range(0, (N-1)*2, 2):
    a += 1
    crossline[a] = line[li+1]
bfs(1)
print(ans)