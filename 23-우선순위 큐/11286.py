from sys import stdin
from bisect import bisect_left

def pop(absHeap, valueHeap):
    if len(absHeap) == 0:
        print(0)
        return absHeap, valueHeap
    result = valueHeap.pop(0)
    absHeap.pop(0)
    print(result)
    return absHeap, valueHeap

def push(n, absHeap, valueHeap):

    index = bisect_left(absHeap, abs(n))
    absHeap.insert(index, n)
    valueHeap.insert(index, n)
    return absHeap, valueHeap

def main():
    N = int(stdin.readline())
    data = [int(stdin.readline().strip()) for i in range(N)]
    valueHeap = []
    absHeap = []
    
    for x in data:
        if x == 0:
            absHeap, valueHeap = pop(absHeap, valueHeap)
        else:
            absHeap, valueHeap = push(x, absHeap, valueHeap)

    # 절대값 고려해서 push or pop하되 뽑아서 출력할 때는 원본 값

if __name__ == "__main__":
    main()