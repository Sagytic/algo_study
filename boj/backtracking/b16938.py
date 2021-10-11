import sys
from pprint import pprint
import copy
sys.stdin = open('input.txt')

NLRX = list(map(int, input().split()))  # N : 문제수 / L : 최소레벨 / R : 최대레벨 / X : 레벨격차 (크같)
level = sorted(list(map(int, input().split())))
ans = 0

for i in range(1 << NLRX[0]):
    cnt = 0
    total = 0
    level1 = 987654321
    level2 = 0
    for j in range(NLRX[0]):
        if i & (1 << j):
            total += level[j]
            cnt += 1
            level1 = min(level1, level[j])
            level2 = max(level2, level[j])
    if cnt >= 2 and level2 - level1 >= NLRX[3] and NLRX[1] <= total <= NLRX[2]:
        ans+=1
print(ans)




