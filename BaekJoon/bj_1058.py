import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
    graph.append(sys.stdin.readline())

result = [[0] * N for _ in range(N)]
q = deque()
answer = []

for i in range(N):
    visited = [False] * N
    q.append((i,0))
    visited[i] = True
    cnt = 0
    while q:
        x, y = q.popleft()

        if y >= 2:
            continue
        
        for j in range(N):
            if graph[x][j] == 'Y' and visited[j] == False:
                cnt += 1
                visited[j] = True
                q.append((j,y+1))
    answer.append(cnt)

print(max(answer))