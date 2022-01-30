def d(maker):
    sum = maker
    maker = str(maker)

    for i in range(0, len(maker)):
        sum += int(maker[i])
    return sum

def main():
    for i in range(1,10001):
        flag = 0
        for j in range(1, i):
            if i == d(j):
                flag = 1
                break
        if flag == 0:
            print(i)

if __name__ == "__main__":
    main()