N = int(input())
num = []

for i in range(N):
    temp = int(input())
    num.append(temp)

num.sort()

for i in num:
    print(i)
