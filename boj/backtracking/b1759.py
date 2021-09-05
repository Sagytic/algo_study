import sys
sys.stdin = open('input.txt')

def check(a, spoint):
    if a >= L:
        sencnt = 0
        tecnt = 0
        for i in box:
            if i in sen:
                sencnt += 1
            else:
                tecnt += 1
        if sencnt and tecnt >= 2:
            for b in box:
                print(b, end='')
            print()
        return
    else:
        for j in range(spoint, C):
            box.append(text[j])
            check(a+1, j+1)
            box.pop()
L, C = map(int, input().split())
text = sorted(list(map(str, input().split())))
sen = ['a', 'e', 'i', 'o', 'u']
box = []
check(0, 0)