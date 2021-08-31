import sys
sys.stdin = open('input.txt')

N = int(input())
layer = [input() for _ in range(N)]
friend = [[0]*N for _ in range(N)]
maxnum = 0

for i in range(N):
    for j in range(N):
        if layer[i][j] == 'Y':
            friend[i][j] = 1
            for k in range(N):
                if i == k:
                    continue
                elif layer[j][k] == 'Y':
                    friend[i][k] = 1
for i in range(N):
    if sum(friend[i]) > maxnum:
        maxnum = sum(friend[i])
print(maxnum)
