import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    price_sort = list(map(int, input().split()))
    stack = []
    while len(stack) < N:
        dcp = price_sort.pop(0)
        for i in range(len(price_sort)):
            if price_sort[i] == int(dcp/3*4):
                price_sort.pop(i)
                stack.append(dcp)
                break
    print('Case #{}: '.format(tc), end='')
    print(*stack)
