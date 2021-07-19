import sys
from collections import Counter

N = int(sys.stdin.readline())
num = []

for i in range(N):
    num.append(int(sys.stdin.readline()))

if(N == 1):
    print(num[0])
    print(num[0])
    print(num[0])
    print(int(0))

else:
    print(round(sum(num)/N))                # 소수점 첫째자리에서 반올림한 값 -> round(sum/N,1)

    num.sort()

    print(num[(N//2)])
    cnt = Counter(num)
    count = cnt.most_common()

    if(count[0][1] == count[1][1]):
        print(count[1][0])
    else:
        print(count[0][0])

    print(num[N-1]-num[0])

