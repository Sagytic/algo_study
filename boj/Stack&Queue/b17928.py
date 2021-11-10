
# 미해결

N = int(input())
li = list(map(int, input().split()))
stack = []
ans = [0]*N

for i in range(N):
    if stack:
        if li[stack[-1]] >= li[i]:
            stack.append(i)
        else:
            while stack and li[stack[-1]] < li[i]:
                tmp = stack.pop()
                ans[tmp] = li[i]
            stack.append(i)
    else:
        stack.append(i)


# while li:
#     tmp = li.pop(0)
#     flag = True
#     if not len(li):
#         ans.append(-1)
#     else:
#         for i in li:
#             if tmp < i:
#                 ans.append(i)
#                 flag = False
#                 break
#         if flag:
#             ans.append(-1)
print(*ans)