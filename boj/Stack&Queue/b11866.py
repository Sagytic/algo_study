inp = list(map(int, input().split()))
N, K = inp[0], inp[1]
li = [_ for _ in range(1, N+1)]
ans = []
popnum = 0
while li:
    popnum += (K-1)
    if popnum >= len(li):
        popnum %= len(li)
    ans.append(str(li.pop(popnum)))
print("<" + ', '.join(ans) + ">")