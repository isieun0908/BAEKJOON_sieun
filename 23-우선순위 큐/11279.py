def pop(maxHeap):
    if len(maxHeap) == 0:
        return 0, maxHeap
    maxV = max(maxHeap)
    maxHeap.remove(maxV)
    return maxV, maxHeap

def push(x, maxHeap):
    maxHeap.append(x)
    return maxHeap

def main():
    N = int(input())
    maxHeap = []
    for n in range(N):
        x = int(input())
        if x == 0:
            result, maxHeap = pop(maxHeap)
            print(result)
        else:
            maxHeap = push(x, maxHeap)

if __name__ == "__main__":
    main()