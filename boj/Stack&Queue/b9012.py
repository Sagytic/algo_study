T = int(input())
VPS = [list(input()) for _ in range(T)]
ans = []
flag = True
for i in range(T):
    flag = True
    stack = []
    for j in VPS[i]:
        if j == '(':
            stack.append(j)
        else:
            if not stack:
                ans.append('NO')
                flag = False
                break
            else:
                stack.pop()
    if flag and not stack:
        ans.append('YES')
    elif flag:
        ans.append('NO')
for _ in ans:
    print(_)
