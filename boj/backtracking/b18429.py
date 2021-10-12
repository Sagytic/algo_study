import sys
from itertools import permutations
sys.stdin = open('input.txt')

def check(cnt, abil):
    global ans
    if cnt == N:
        ans += 1
        return
    if abil < 500:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            check(cnt+1, abil-K+kit[i])
            visited[i] = 0
    return

ans = 0
N, K = map(int, input().split())
kit = list(map(int, input().split()))
visited = [0] * N
check(0, 500)
print(ans)





# comb = permutations(kit, 3)
#
# for i in comb:
#     ability = 500
#     for j in i:
#         ability += (j - K)
#         if ability < 500:
#             break
#     if ability >= 500:
#         ans += 1
# print(ans)
