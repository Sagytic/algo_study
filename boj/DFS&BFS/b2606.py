import sys
from pprint import pprint
sys.stdin =open('input.txt')

def virus(v):
    stuff = []
    stuff.append(v)
    visited[v] = 1
    cnt = 0
    while stuff:
        s = stuff.pop(0)
        for i in range(1, V+1):
            if adj[s][i] and not visited[i]:
                stuff.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

V = int(input())
E = int(input())
network = [list(map(int, input().split())) for _ in range(E)]
adj = [[0] * (V+1) for _ in range(V+1)]
visited = [0]*(V+1)
for i in range(E):
    n1, n2 = network[i][0], network[i][1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

print(virus(1))