from sys import stdin
from bisect import bisect_left

def pop(minHeap):
    if len(minHeap) == 0:
        print(0)
        return minHeap
    result = minHeap.pop(0)
    print(result)
    return minHeap

def push(n, minHeap):
    index = bisect_left(minHeap, n)
    minHeap.insert(index, n)
    return minHeap

def main():
    N = int(stdin.readline())
    data = [int(stdin.readline().strip()) for i in range(N)]
    minHeap = []
    
    for x in data:
        if x == 0:
            minHeap = pop(minHeap)
        else:
            minHeap = push(x, minHeap)

if __name__ == "__main__":
    main()