from sys import stdin

visited = []
count = 0

def bfs(V, E, R):
    global count
    count += 1
    visited[R-1] = count

    queueBFS = []
    queueBFS.append(R)
    
    closed = []
    while (not (len(queueBFS) == 0)):
        newR = queueBFS.pop(0)

        # 인접 정점 집합 구하기
        closed.clear()
        for i in E:
            if i[0] == newR:
                closed.append(i[1])
        for x in closed:
            if (visited[x-1] == 0):
                count += 1
                visited[x-1] = count
                queueBFS.append(x)

def main():
    N, M, R = map(int, stdin.readline().split())
    edge = [list(map(int, stdin.readline().strip().split())) for i in range(M)]
    
    for i in edge:
        lst = [i[1], i[0]]
        if not lst in edge:
            edge.append(lst)

    for i in range(0, N):
        visited.append(0)

    edge.sort()
    bfs(edge, edge, R)

    for point in visited:
        print(point)

if __name__ == "__main__":
    main()