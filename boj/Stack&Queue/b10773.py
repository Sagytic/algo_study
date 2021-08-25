import sys
sys.stdin = open('input.txt')

N = int(input())
account = []
ls = []
for i in range(K):
    inn = int(input())
    if inn:
        account.append(inn)
    else:
        account.pop()
print(sum(account))
    