
# 미해결

N = int(input())
li = list(map(int, input().split()))
ans = []

while li:
    tmp = li.pop(0)
    flag = True
    if not len(li):
        ans.append(-1)
    else:
        for i in li:
            if tmp < i:
                ans.append(i)
                flag = False
                break
        if flag:
            ans.append(-1)

print(*ans)