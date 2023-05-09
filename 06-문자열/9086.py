import sys

def main():
    T = int(sys.stdin.readline().strip())

    for i in range(T):
        word = sys.stdin.readline().strip()
        print(word[0], end='')
        print(word[len(word)-1])

if __name__ == "__main__":
    main()