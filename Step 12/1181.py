def main():
    N = int(input())
    alpha = {}

    for i in range(0, N):
        word = input()
        alpha[word] = len(word)

    i = 1
    while len(alpha) > 0:
        list = []
        for j in alpha:
            if alpha[j] == i:
                list.append(j)
        for j in list:
            alpha.pop(j)
        list.sort()
        for j in list:
            print(j)
        i += 1

if __name__ == "__main__":
    main()