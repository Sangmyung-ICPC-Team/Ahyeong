from collections import deque

def init(V):
    visited = [False for _ in range(V+1)] 
    return visited

def insert_edge(V, E):
    adj_mat = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for edge in E:
        adj_mat[edge[0]][edge[1]] = 1
        adj_mat[edge[1]][edge[0]] = 1

    return adj_mat

def bfs(V, adj_mat, vertex, visited):
    cnt = 0
    visited[vertex] = True

    queue = deque()
    queue.append(vertex)

    while queue:
        vertex = queue.popleft()
        for i in range(V+1):
            if adj_mat[vertex][i] == 1 and visited[i] == False:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt
        
if __name__ == "__main__":
    V = int(input()) 
    E = int(input()) 
    E = [list(map(int, input().split())) for _ in range(E)] 
    
    adj_mat = insert_edge(V,E)
    visited = init(V)

    print(bfs(V, adj_mat, 1, visited))