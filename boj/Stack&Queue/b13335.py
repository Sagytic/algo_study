from collections import deque
n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque(0 for _ in range(w))
bridge_weight = 0
cnt = 0

while bridge or trucks:
    cnt += 1
    bridge_weight -= bridge.popleft()
    if trucks:
        if bridge_weight + trucks[0] <= l:
            newone = trucks.popleft()
            bridge.append(newone)
            bridge_weight += newone
        else:
            bridge.append(0)
print(cnt)