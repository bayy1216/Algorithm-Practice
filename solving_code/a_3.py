import sys

N = int(sys.argv[1])


def move(before, after, what):
    print(f"{before}번 기둥에서 {after}번 기둥으로 {what}번 원판 이동")


def hanoi(n, before, to, after):
    if n == 1:
        move(before, after, n)#출발지에서 목적지로
        return

    hanoi(n - 1, before, after, to)  # n-1개 원판을 이동전에서 경유지로
    move(before, after, n)  # n번원판을 목적지로
    hanoi(n - 1, to, before, after)  # n-1개 원판을 경유지에서 목적지로


hanoi(N, 1, 2, 3)
