import sys
sys.stdin = open('input.txt')
input=sys.stdin.readline
n,m=map(int,input().split())
result=0
stack=[[] for _ in range(7)]

for _ in range(n):
    flag = True
    a, p = map(int,input().split())
    while stack[a] and stack[a][-1] >= p:
        if stack[a][-1] == p:
          flag = False
          break
        stack[a].pop()
        result+=1
    if flag==False:
        continue
    stack[a].append(p)
    result+=1
print(result)