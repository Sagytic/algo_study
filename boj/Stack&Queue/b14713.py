from collections import deque
N = int(input())
S = []
for _ in range(N):
    S.append(deque(input().split()))
L = deque(list(input().split()))
cnt = 0
while L:
    if cnt >= N:
        break
    for i in S:
        if i and L and i[0] == L[0]:
            i.popleft()
            L.popleft()
            cnt = 0
            break
        else:
            cnt += 1
ans = ''
if L or (cnt >= N):
    ans = 'Impossible'
else:
    ans = 'Possible'
for i in S:
    if len(i):
        ans = 'Impossible'
        break
print(ans)