from collections import deque #load deque

global cnt
cnt = 0

def init(V):
    visited = [False for _ in range(V+1)] #1차원 배열 생성
    return visited

def insert_edge(V, E):
    adj_mat = [[0 for _ in range(V+1)] for _ in range(V+1)] # 2차원 배열 생성

    for edge in E: # [[1,0], [2,0], [1,2]]
        adj_mat[edge[0]][edge[1]] = 1
        adj_mat[edge[1]][edge[0]] = 1
    return adj_mat

def breath_first_search(V, adj_mat, vertex, visited):
    global cnt
    visited[vertex] = True

    queue = deque()
    queue.append(vertex) #enqueue

    while queue:
        vertex = queue.popleft() #dequeue
        for i in range(V+1):
            if adj_mat[vertex][i] == 1 and visited[i] == False:
                visited[i] = True
                cnt += 1
                queue.append(i)
        
if __name__ == "__main__":
    V = int(input()) 
    E = int(input()) 
    E = [list(map(int, input().split())) for _ in range(E)]  # 0110 -> [[0,1,1,0]]
    adj_mat = insert_edge(V,E)
    visited = init(V)
    breath_first_search(V, adj_mat, 1, visited)
    print(cnt)