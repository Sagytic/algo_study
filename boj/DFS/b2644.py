import sys
sys.stdin =open('input.txt')

def cousin(v):
    next = []
    next.append(v)
    visited[v] = 1
    cnt = 0
    while next:
        s = next.pop(0)
        for i in range(1, V+1):
            if adj[s][i] and not visited[i]:
                next.append(i)
                visited[i] = visited[s] + 1
                cnt += 1
                if i == G:
                    return visited[i] -1
    return -1

V = int(input())
S, G = map(int, input().split())
E = int(input())
fam = [list(map(int, input().split())) for _ in range(E)]
adj = [[0] * (V+1) for _ in range(V+1)]
visited = [0]*(V+1)
for i in range(E):
    n1, n2 = fam[i][0], fam[i][1]
    adj[n1][n2] = adj[n2][n1] = 1

print(cousin(S))