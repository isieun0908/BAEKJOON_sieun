def insertion_sort(N):
    list = []
    for i in range(0, N):
        num = int(input())
        flag = 1
        for j in range(0, len(list)):
            if list[j] >= num:
                list.insert(j, num)
                flag = 0
                break
        if flag:
            list.append(num)
    for i in range(0, N):
        print(list[i])

def bubble_sort(N):
    list = []
    for i in range(0, N):
        list.append(int(input()))
    flag = 1
    while flag:
        flag = 0
        for i in range(0,N-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                flag = 1
    for i in range(0, N):
        print(list[i])

def main():
    N = int(input())
    #insertion_sort(N)
    bubble_sort(N)

if __name__ == "__main__":
    main()