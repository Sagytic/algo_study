N, D = map(int, input().split())
shortcut = sorted([list(map(int, input().split())) for _ in range(N)])
for i in shortcut:
    if i[1] > D:
        shortcut.remove(i)
ans = 0
dis = [_ for _ in range(10001)]

for i in range(D+1):
    if dis[i] > dis[i-1]+1:
        dis[i] = dis[i-1]+1
    for j in shortcut:
        if i == j[0]:
            if dis[j[1]] > (dis[i] + j[2]):
                dis[j[1]] = (dis[i] + j[2])
print(dis[D])
