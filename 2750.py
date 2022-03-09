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

def main():
    N = int(input())
    insertion_sort(N)

if __name__ == "__main__":
    main()