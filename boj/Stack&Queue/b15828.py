# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline
# stack = []
# n = input()
# while True:
#     tmp = int(input())
#     if tmp:
#         stack.append(tmp)
#     elif not tmp:
#         stack.pop(0)
#     if tmp == -1:
#         break
# stack.pop()
# if stack:
#     print(*stack)
# else:
#     print('empty')

from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = input()
q = deque()
while True:
    tmp = int(input())
    if tmp == -1: break
    if tmp: q.append(tmp)
    else: q.popleft()
if q: print(*q)
else: print('empty')