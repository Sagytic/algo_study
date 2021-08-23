import sys
sys.stdin = open('input.txt')
from collections import deque

# 시간초과
# ls = []
# for _ in range(int(input()),0, -1):
#     ls.append(_)
# while True:
#     ls.pop()
#     if len(ls) == 1:
#         break
#     last_num = [ls[len(ls)-1]]
#     ls.pop()
#     ls = last_num + ls
# print(*ls)

# deque 활용하여 처리
# 양쪽 끝에서 삽입 / 삭제 가능(큐, 스택과 비슷)
# append(val) : deque의 제일 마지막 부분에 val 값을 추가(오른쪽 끝)
# appendleft(val) : deque는 양쪽 끝에서 삽입,삭제가 가능하기에, deque 시작 부분에 val 값 추가(왼쪽 끝)
# extend(dest) : list와 마찬가지로 마지막 부분에 병합시켜준다
# extendleft(dest) : 시작 부분에 병합시켜준다
# pop() : deque 제일 마지막 부분부터 하나씩 추출 및 삭제한다(오른쪽 끝부터)
# popleft() : deque 시작 부분부터 하나씩 추출 및 삭제한다(왼쪽 부터)
# rotate(count) : count만큼 deque 값들을 회전, 음수면 왼쪽, 양수면 오른쪽으로 회전

deq = deque([i for i in range(1, int(input())+1)])
while len(deq) > 1:
    deq.popleft()               # 제일 왼쪽값 추출 및 삭제 1
    deq.append(deq.popleft())   # 맨 끝에 값 추가          2
print(deq.pop())
#################################
#           1                   #
#           2                   #
#           3                   #
#           4                   #
#           5                   #
#           6                   #
#################################
#################################
#           3                   #
#           4                   #
#           5                   #
#           6                   #
#           2                   #
#################################
#################################
#           5                   #
#           6                   #
#           2                   #
#           4                   #
#################################
#################################
#           2                   #
#           4                   #
#           6                   #
#################################
#################################
#           6                   #
#           4                   #
#################################
#################################
#           6                   #
#################################