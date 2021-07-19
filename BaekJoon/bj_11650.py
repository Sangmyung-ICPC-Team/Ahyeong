import sys

N = int(sys.stdin.readline())

coordinate = []
for i in range(N):
    coordinate.append(list(map(int, input().split())))

coordinate.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(coordinate[i][0],coordinate[i][1])