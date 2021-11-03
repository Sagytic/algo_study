N, K = map(int, (input().split()))

table = list(input())
ans = 0

for i in range(len(table)):
    if table[i] == 'P':
        left = i - K
        right = i + K
        left = 0 if left < 0 else left
        right = N-1 if right > N-1 else right
        for j in range(left, right+1):
            if table[j] == 'H':
                table[j] = ''
                ans += 1
                break
print(ans)