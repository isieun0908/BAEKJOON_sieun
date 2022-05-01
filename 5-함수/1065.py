def hansu(num):
    list = []

    while num >= 1:
        list.append(num%10)
        num = int(num / 10)
    if len(list) == 1:
        return 1
    distance = list[0] - list[1]
    for i in range(1, len(list)-1):
        if not list[i] - list[i+1] == distance:
            return 0
    return 1

def main():
    N = int(input())

    count = 0
    for i in range(1, N+1):
        if hansu(i):
            count += 1
    print(count)

if __name__ == "__main__":
    main()