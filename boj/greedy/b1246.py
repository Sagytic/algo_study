N, M = map(int, input().split())
price = sorted([int(input()) for _ in range(M)])
ans, ans_cost = 0, 0
for i in range(1, M+1):
    egg = i
    if egg > N:
        egg = N
    new_price = price[-i] * egg
    if new_price > ans:
        ans = new_price
        ans_cost = price[-i]
print(ans_cost, ans)