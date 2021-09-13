import sys
sys.stdin = open('input.txt')

def check(start, end, level):
    if start == end:
        li[level].append(tree[start])
        return
    middle = (start + end) // 2
    li[level].append(tree[middle])
    check(start, middle - 1, level+1)
    check(middle+1, end, level+1)
K = int(input())
tree = list(map(int, (input().split())))
length = len(tree)
level = 0
li = [[] for _ in range(K)]
check(0, length-1, 0)
# print(li)
for i in li:
    print(*i)
# while True:
#     li[level].append(tree[(length//2) +1])
#     level += 1
