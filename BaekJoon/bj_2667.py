from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def init(N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    return visited

def bfs(matrix, visited, i, j, N):
    queue = deque()
    visited[i][j] = True
    queue.append([i, j])
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if  0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and matrix[nx][ny] == '1':
                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt += 1
    return cnt
        
    
if __name__ == "__main__":
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    visited = init(N)
    num = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '1' and visited[i][j] == False:
                num.append(bfs(matrix, visited, i, j, N))

    num.sort()
    print(len(num))
    for i in num:
        print(i)

