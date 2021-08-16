import sys

def dfs(x, y):
    visited[x][y] = True

    dx = [0, 0, -1, 1, -1, -1, 1, 1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)


if __name__ == "__main__":
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0:
            break

        graph = []
        for i in range(h):
            graph.append(list(map(int, sys.stdin.readline().split())))

        visited = [[False for _ in range(w)] for _ in range(h)]

        cnt = 0

        for i in range(h):
            for j in range(w):
                if visited[i][j] == False and graph[i][j] == 1:
                    dfs(i,j)
                    cnt += 1
        print(cnt)


