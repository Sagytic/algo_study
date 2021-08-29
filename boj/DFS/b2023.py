import sys
sys.stdin =open('input.txt')

def check(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if i**2 > n:
            break
        if n % i == 0:
            return False
    return True
n = int(input())
f = [2, 3, 5, 7]
stk = []
for i in range(n-1):
    for j in f:
        for k in range(1, 11, 2):
            if check(int(str(j)+str(k))):
                stk.append(int(str(j)+str(k)))
    while f:
        f.pop()
    for i in stk:
        f.append(i)
    while stk:
        stk.pop()
for i in f:
    print(i)
