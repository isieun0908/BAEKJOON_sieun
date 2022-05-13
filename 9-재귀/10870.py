def fibonachi(fibo):
    if fibo <= 0:
        return 0
    elif fibo == 1:
        return 1
    return fibonachi(fibo-1) + fibonachi(fibo-2)

def main():
    n = int(input())
    print(fibonachi(n))

if __name__ == "__main__":
    main()