import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    li = [0 for _ in range(N)]
    cnt = 1
    for i in range(N):
        a, b = map(int, input().split())
        li[a-1] = b

    minrev = li[0]
    for j in range(1, N):
        if li[j] < minrev:
            cnt += 1
            minrev = li[j]

    print(cnt)
