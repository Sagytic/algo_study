import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque

N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))
ans = 0
for i in range(len(A)):
    ans += A[i]*B[i]
print(ans)