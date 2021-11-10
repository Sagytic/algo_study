import sys
from pprint import pprint
from copy import deepcopy
from itertools import permutations
from collections import deque

sys.stdin = open('input.txt')

N = int(input())
li = list(map(int, input().split()))
stack = []
ans = [-1]*N
for i in range(N):
    if stack:
        if li[stack[-1]] >= li[i]:
            stack.append(i)
        else:
            while stack and li[stack[-1]] < li[i]:
                tmp = stack.pop()
                ans[tmp] = li[i]
            stack.append(i)
    else:
        stack.append(i)
print(*ans)