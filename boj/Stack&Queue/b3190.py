import sys
sys.setrecursionlimit(1000000)
# dir:0 -> 우 / 1: 하 / 2: 좌 / 3: 상
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]

def D_irection(dir_head_change):
    if dir_head_change == 3:
        return 0
    return dir_head_change + 1

def L_irection(dir_head_change):
    if dir_head_change == 0:
        return 3
    return dir_head_change - 1

def Dummy(x, y, time, dir_head): # x좌표, y좌표, 시간, 방향
    global ans, board
    head = [x, y]   # 머리 좌표
    snake.append(head)  # 뱀 길이에 머리 추가

    if direction and time == int(direction[0][0]): # 방향 변경
        if direction[0][1] == 'D':
            dir_head = D_irection(dir_head)
        else:
            dir_head = L_irection(dir_head)
        direction.pop(0)

    Nhead_x = x + nx[dir_head]  # 새 머리위치
    Nhead_y = y + ny[dir_head]  # 새 머리위치

    if 0 <= Nhead_y < N and 0 <= Nhead_x < N:   # 새 머리가 board 안 벗어나면 그대로
        pass
    else:                                       # 벗어나면 그 다음턴에 죽으니까 시간 +1 하고 리턴
        ans = time + 1
        return

    if [Nhead_x, Nhead_y] in snake:                     # 새 머리가 몸 박으면 다음턴 죽으니 시간 +1 리턴
        ans = time + 1
        return

    if board[Nhead_y][Nhead_x] == 'a':          # 새 머리가 사과를 먹으면
        board[Nhead_y][Nhead_x] = 0            # 사과 없애고 꼬리 남기고
        # print(board[Nhead_y][Nhead_x])          # 사과 먹고 왜 0으로 안 바꿔주지?
    else:                                       # 사과 못 먹으면
        snake.pop(0)                            # 꼬리부분 삭제

    if Nhead_x < 0 or Nhead_x == N or Nhead_y < 0 or Nhead_y == N:  # 새 머리 -> 벽박으면 시간+1 보내면서 죽고 리턴
        ans = time + 1
        return

    Dummy(Nhead_x, Nhead_y, time+1, dir_head)   # 다 정상이면 시간+1 하고 새 머리로 좌표 보내기
    return

N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)] # 사과의 위치
L = int(input())
direction = [list(input().split()) for _ in range(L)] # 뱀의 방향 변환 [0]초 후 [1]가 L이면 왼 D면 오른으로 90도 회전
board = [[0] * N for _ in range(N)]
ans = 0
for i in apple:
    board[i[0]-1][i[1]-1] = 'a'
direction_head = 0
snake = []

# pprint(board)
# pprint(direction)
Dummy(0, 0, 0, 0) # x좌표, y좌표, 시간, 방향
print(ans)
# pprint(board)



'''
def D_irection(dir_head_change):
    if dir_head_change == 3:
        return 0
    return dir_head_change + 1

def L_irection(dir_head_change):
    if dir_head_change == 0:
        return 3
    return dir_head_change - 1
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]
N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
direction = [list(input().split()) for _ in range(L)]
board = [[0] * N for _ in range(N)]
ans = 0
for i in apple:
    board[i[0]-1][i[1]-1] = 'a'
direction_head = 0
snake = [[0, 0]]
time = 0
x = snake[-1][0]
y = snake[-1][1]

while True:
    time += 1
    x = x + nx[direction_head]
    y = x + nx[direction_head]

    # 새로운 방향의 머리가 board의 범위를 벗어나는가 ?
    if 0 <= x < N and 0 <= y < N:   # 새 머리가 board 안 벗어나면 그대로
        pass
    else:                                       # 벗어나면 그 다음턴에 죽으니까 시간 +1 하고 리턴
        ans = time + 1
        break
    # 꼬리 ~ 몸통에 머리를 박는가 ?
    if [x, y] in snake:                     # 새 머리가 몸 박으면 다음턴 죽으니 시간 +1 리턴
        ans = time + 1
        break
    # 갈 수 있다면 가면서 내 몸 리스트에 새로운 머리를 추가
    snake.append([x, y])

    # 사과 여부 판단
    if board[x][y] == 'a':          # 새 머리가 사과를 먹으면
        board[x][y] = 0            # 사과 없애고 꼬리 남기고
        print(board[x][y])          # 사과 먹고 왜 0으로 안 바꿔주지?
    else:                                       # 사과 못 먹으면
        snake.pop(0)                            # 꼬리부분 삭제

    # 새로운 머리의 방향을 정해야 하는가 ?
    if direction and time == int(direction[0][0]): # 방향 변경
        if direction[0][1] == 'D':
            dir_head = D_irection(direction_head)
        else:
            dir_head = L_irection(direction_head)
        direction.pop(0)
pprint(board)
print(ans)
'''