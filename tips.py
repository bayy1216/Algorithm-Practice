import sys
from itertools import permutations, combinations, product, combinations_with_replacement
import heapq
from bisect import bisect_left, bisect_right
from collections import deque, Counter

input1 = sys.stdin.readline().rstrip()  # 빠른 입력속도

M, N, H = map(int, input().split())
inputList = list(map(int, input().split()))
result = eval("3*5+7")  # 문자열 형태의 수식 계산
resultAry = sorted([8, 4, 3, 9, 7, 2, 6], reverse=True)  # iterable 객체의 입력을 정렬된 결과로 반환

ary = [[[0] * N for _ in range(M)] for _ in range(H)]  # 배열 생성 짧은 코드

data1 = ['A', 'B', 'C']

result1 = list(permutations(data1, 3))  # data1의 모든 순열 구하기(순서있는 나열 경우의 수)
result2 = list(combinations(data1, 2))  # data1의 2개뽑는 모든 조합 구하기(순서없는 나열 경우의수)
result3 = list(product(data1, repeat=2))  # data1의 2개뽑는 순열 구하기(순서,중복 있는 나열  경우의 수)
result4 = list(combinations_with_replacement(data1, 2))  # data1의 2개뽑는 모든 조합 구하기(순서없는,중복있는 나열 경우의수)

# MinHeap 사용
h = []
res = []
value = list(map(int, input().split()))
for v in value:
    heapq.heappush(h, v)
for _ in range(len(h)):
    res.append(heapq.heappop(h))
# MaxHeap 사용법    Push할떄 -1곱하고    POP할때 -1곱해서 원래대로 해준다


aa = [1, 2, 4, 4, 8]

i1 = bisect_left(aa, 2)  # 정렬된 배열에서 정렬된 순서를 유지하면서 리스트a에 데이터x를 삽일할 가장 왼쪽 인덱스

i2 = bisect_right(aa, 2)  # 정렬된 배열에서 정렬된 순서를 유지하면서 리스트a에 데이터x를 삽일할 가장 오른쪽 인덱스
# 이를 통해  a<= x <= b에서 x의 원소의 개수를 logN으로 찾을 수 있다.

#deque
data11 = deque([2,3,4])
data11.append(4)
data11.appendleft(4)
data11.pop()
data11.popleft()

counter = Counter(['g','r','g','b','b','r','b'])
a = counter['r'] #a=2
b = counter['b'] #b=3





ary1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ary2 = [3, 5]
ary3 = [i for i in ary1 if i not in ary2]  # 특정한 원소제거하는법

tup = (1, 2, 3, 4)  # 튜플 사용법. 변경불가

data_set = {1, 1, 2, 3, 4, 4, 5}  # data_set = set([1, 1, 2, 3, 4, 4, 5]) 집합 사용법
# 연산은 a|b합집합     a&b 교집합  a-b 차집합

data = dict()  # 사전 사용방법
data['사과'] = 'apple'
data['바나나'] = 'banana'
key_list = data.keys()
value_list = data.values()
for key in key_list:
    print(data[key])
