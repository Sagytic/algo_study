from copy import deepcopy
def bulb_switch(n, li):
    if n == N-1:
        li[n-1] = 1 if not li[n-1] else 0
        li[n] = 1 if not li[n] else 0
    else:
        li[n-1] = 1 if not li[n-1] else 0
        li[n] = 1 if not li[n] else 0
        li[n+1] = 1 if not li[n+1] else 0

N = int(input())
bulb1 = list(map(int, input()))
bulb2 = deepcopy(bulb1)
goal = list(map(int, input()))
ans1 = 1
ans2 = 0

# case1
bulb1[0] = 1 if not bulb1[0] else 0
bulb1[1] = 1 if not bulb1[1] else 0
for i in range(1, N):
    if bulb1[i-1] != goal[i-1]:
        ans1 += 1
        bulb_switch(i, bulb1)
    if bulb2[i-1] != goal[i-1]:
        ans2 += 1
        bulb_switch(i, bulb2)
if bulb1 != goal:
    ans1 = -1
if bulb2 != goal:
    ans2 = -1

if ans1 == -1 and ans2 == -1:
    print(-1)
elif ans1 == -1:
    print(ans2)
elif ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))