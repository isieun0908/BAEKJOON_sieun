def main():
    one, second, third = map(int, input().split())
    if one == second and one == third:
        print(10000+one*1000)
    elif one == second or one == third:
        print(1000+one*100)
    elif second == third:
        print(1000 + second * 100)
    else:
        print(max(one, second, third)*100)

if __name__ == "__main__":
    main()