def merge_sort(list):
    print(list)

def main():
    N = int(input())
    list =[]

    for i in range(0, N):
        list.append(int(input()))
    merge_sort(list)

if __name__ == "__main__":
    main()