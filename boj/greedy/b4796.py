import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int, input().split()) # L: 사용 가능 일 / P : 연속하는 캠핑일 / V : 휴가일
    if not L:
        break
    ans = 0
    minans = V%P
    if L < V%P:
        minans = L
    ans += (((V//P)*L) + minans)
    print(f'Case {i}: {ans}')
    i += 1