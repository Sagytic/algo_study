import sys
sys.stdin = open('input.txt')

K = int(input())
account = []
ls = []
for i in range(K):
    inn = int(input())
    if inn:
        account.append(inn)
    else:
        account.pop()
print(sum(account))
    