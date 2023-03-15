'''
별다른 풀이해법을 찾지못해 브루트포스로 모든경우를 다찾는방식으로 접근하였다
'''

def solv(n1, n2):
    a = n1
    b = n2
    aryA = [a]
    aryB = [b]

    countC = -1
    while a != 1:
        if a % 2 == 0:
            a /= 2
        else:
            a = 3 * a + 1
        aryA.append(a)
    while b != 1:
        if b % 2 == 0:
            b /= 2
        else:
            b = 3 * b + 1
        aryB.append(b)

    for index_a in range(len(aryA)):
        for index_b in range(len(aryB)):
            if aryA[index_a] == aryB[index_b]:
                countC = aryA[index_a]
                return "%d needs %d steps, %d needs %d steps, they meet at %d" % (n1, index_a, n2, index_b, countC)


while True:
    A, B = map(int, input().split())
    if (A == 0 and B == 0):
        break
    print(solv(A, B))
