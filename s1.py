import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque

stick = list(input())
ans = 0
stack = []

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append('(')
    else:
        if stick[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)