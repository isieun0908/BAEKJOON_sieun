def main():
    S = input()

    for i in range(97, 122+1):
        print(S.find(chr(i)), end=' ')

if __name__ == "__main__":
    main()