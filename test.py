import sys
from pprint import pprint
import copy
from itertools import permutations
sys.stdin = open('input.txt')




N=int(input());li=[list(map(int, input().split())) for _ in range(N)];
for i in li:
 lv=1;
 for j in li:
   if i[0]<j[0] and i[1]<j[1]:
     lv+=1
 print(lv,end=' ')




