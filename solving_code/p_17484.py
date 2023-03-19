'''
DFS관련 문제인것을 알았지만 별다른 풀이법이 생각안나 지나간 경로를 문자열로 표현하여 dict로 표현하였음
'''
N, M = map(int, input().split())
ary = []
for _ in range(N):
    ary.append(list(map(int, input().split())))
moveHistory = dict()

dap = []

def move(x, y, moveD, history):
    dx = x
    dy = y + 1
    if moveD == 0:
        dx = dx - 1
    elif moveD == 2:
        dx = dx + 1

    if dx < 0 or dx > M-1:
        return

    currHistory = history + str(moveD)


    moveHistory[currHistory] = moveHistory[history] + ary[dy][dx]

    if dy == N-1:
        dap.append(moveHistory[currHistory])
        return

    for i in range(3):
        if moveD == i:
            continue
        move(dx, dy, i, currHistory)


for i in range(M):
    moveHistory[str(i)] = ary[0][i]
    for j in range(3):
        move(i, 0, j, str(i))

print(min(dap))