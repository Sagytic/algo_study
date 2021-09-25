import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
R = [[0, 0]] + [[0, int(input())] for _ in range(N)]
W = [0] + [int(input()) for _ in range(M)]
inout = [int(input()) for _ in range(2*M)]
Q = []
q, ans = 0, 0
for io in inout:
    if io > 0:
        for r in range(1, N+1):
            if not R[r][0]:
                R[r][0] = io
                ans += R[r][1] * W[io]
                break
        else:
            Q.append(io)
    else:
        for r in range(1, N+1):
            if R[r][0] == -io:
                if len(Q) != q:
                    R[r][0] = Q[q]
                    ans += R[r][1] * W[Q[q]]
                    q += 1
                else:
                    R[r][0] = 0
print(ans)