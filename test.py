import sys
from pprint import pprint
from copy import deepcopy
from itertools import permutations
from collections import deque

sys.stdin = open('input.txt')

from collections import deque
'''

N = int(input())
S = [list(input().split()) for _ in range(N)]
L = list(input().split())

for i in L:
    for j in S:
        if j:
            if j[0] == i:
                j.pop(0)
                break
ans = []
for i in S:
    ans += i

if not ans:
    print('Possible')
else:
    print('Impossible')
'''
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