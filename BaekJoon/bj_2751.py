import sys

N = int(sys.stdin.readline())
num = []

for i in range(N):
    temp = int(sys.stdin.readline())
    num.append(temp)

num.sort()

for i in num:
    print(i)
