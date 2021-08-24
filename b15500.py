import sys
sys.stdin = open('input.txt')

N = int(input())
stack1 = list(map(int, input().split()))
stack2 = []
stack3 = []
klog = []
cnt = 0

while N:
    while stack1:
        if stack1[-1] == N:
            stack3.append(stack1.pop())
            klog.append('1 3')
            N -= 1
            cnt += 1
        else:
            stack2.append(stack1.pop())
            klog.append('1 2')
            cnt += 1
    while stack2:
        if stack2[-1] == N:
            stack3.append(stack2.pop())
            klog.append('2 3')
            N -= 1
            cnt += 1
        else:
            stack1.append(stack2.pop())
            klog.append('2 1')
            cnt += 1
print(cnt)
for i in klog:
    print(i)