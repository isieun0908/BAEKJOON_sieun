import sys
from collections import deque

def main():
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())

    visited = [0 for i in range(V+1)]
    edges = [[] for i in range(V+1)]
    
    for e in range(E):
        v1, v2 = map(int, sys.stdin.readline().split())
        edges[v1].append(v2)
        edges[v2].append(v1)
    
    # 정렬
    for edge in edges:
        edge.sort()

    stack = deque([])
    stack.append(1)
    while stack:
        vertice = stack.pop()
        #print(vertice)
        visited[vertice] = 1
        #print(visited)

        for e in edges[vertice]:
            if (visited[e] == 0) and (not e in stack):
                stack.append(e)
        
        #print(stack)

    # 방문 숫자
    count = 0
    for v in visited:
        if v:
            count += 1
    print(count-1)

if __name__ == "__main__":
    main()