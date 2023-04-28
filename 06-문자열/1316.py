def groupWord(word):
    group = {}
    flag = True
    for i in range(0, len(word)):
        if word[i] in group:
            if group[word[i]] == 0:
                flag = False
                break
        else:
            group[word[i]] = 1
        if i + 1 != len(word) and word[i + 1] != word[i]:
            group[word[i]] = 0
    return flag

def main():
    inputNum = int(input())

    count = 0
    for i in range(0, inputNum):
        word = input()
        if groupWord(word):
            count += 1
    print(count)

if __name__ == "__main__":
    main()