from sys import stdin

settingData = [1, 1, 2, 2, 2, 8]

def main():
    inputData = list(map(int, stdin.readline().split()))

    printData = []
    for i in range(6):
        printData.append(settingData[i] - inputData[i])

    print(printData)

if __name__ == "__main__":
    main()