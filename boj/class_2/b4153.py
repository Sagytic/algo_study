import sys
sys.stdin = open('input.txt')
from pprint import pprint


while True:
    tri = sorted(list(map(int, (input().split()))))
    if tri == [0, 0, 0]:
        break
    elif tri[0]**2 + tri[1]**2 == tri[2]**2:
        print('right')
    else:
        print('wrong')
