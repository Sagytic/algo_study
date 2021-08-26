import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline      # input 읽는 시간 단축 시간제한 0.5초였음..
stack = []
def push(item):
    stack.append(item)

def Spop():
    if len(stack):
        return stack.pop()
    else:
        return -1

def size():
    return len(stack)

def empty():
    if size():
        return 0
    else:
        return 1

def top():
    if size():
        return stack[-1]
    else:
        return -1

text = [input().split() for _ in range(int(input()))]
for i in text:
    if i[0] == 'push':
        push(int(i[1]))
    elif i[0] == 'pop':
        print(Spop())
    elif i[0] == 'size':
        print(size())
    elif i[0] == 'empty':
        print(empty())
    elif i[0] == 'top':
        print(top())