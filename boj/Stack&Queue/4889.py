layer = 0
while True:
    layer += 1
    stack = []
    newone = input()
    ans = 0
    if '-' in newone:
        break
    for char in newone:
        if char == '{':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                ans += 1
                stack.append('{')
    ans += len(stack) // 2
    print('{}. {}'.format(layer, ans))