import sys
sys.stdin = open('input.txt')

def order1(n):
    print(n, end='')
    if dic.get(n)[0] != '.':
        order1(dic.get(n)[0])
    if dic.get(n)[1] != '.':
        order1(dic.get(n)[1])
def order2(n):
    if dic.get(n)[0] != '.':
        order2(dic.get(n)[0])
    print(n, end='')
    if dic.get(n)[1] != '.':
        order2(dic.get(n)[1])
def order3(n):
    if dic.get(n)[0] != '.':
        order3(dic.get(n)[0])
    if dic.get(n)[1] != '.':
        order3(dic.get(n)[1])
    print(n, end='')
V = int(input())
edge = [list(input().split()) for _ in range(V)]
dic = {}
for i in range(V):
    dic[edge[i][0]] = edge[i][1], edge[i][2]
order1('A')
print()
order2('A')
print()
order3('A')