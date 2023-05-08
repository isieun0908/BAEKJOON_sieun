import sys
from collections import deque

def main():
    N, M, R = map(int, sys.stdin.readline().split())

    # 정점 & 간선 초기화
    visited = [0 for i in range(N+1)]
    edges = [[] for i in range(N+1)]

    # 간선 입력
    for i in range(M):
        v1, v2 = map(int, sys.stdin.readline().split())
        edges[v1].append(v2)
        edges[v2].append(v1)
        
    # 정렬
    for i in range(N):
        edges[i].sort()
    print(edges)
    print(visited)
    
    # dfs
    stack = deque([])
    stack.append(R)

    result = []
    while stack:
        vertice = stack.pop()
        if visited[vertice] == 1:
            continue
        visited[vertice] = 1
        
        for v in range(len(edges[vertice]), -1,-1):
            if visited[edges[vertice][v]] == 0:
                stack.append(edges[vertice][v])

if __name__ == "__main__":
    main()