import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, Q = map(int, input().split())
wannaNode = [int(input()) for _ in range(Q)]
visited = set()

for i in range(Q):
    duck = wannaNode[i]
    now = duck
    ans = 0
    while now > 1:
        if now in visited:
            ans = now
        now = now//2

    if not ans:
        visited.add(duck)
    print(ans)