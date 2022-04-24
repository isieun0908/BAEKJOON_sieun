def main():
    x_list = []
    y_list = []

    for i in range(0, 3):
        x, y = map(int, input().split())
        if not x in x_list:
            x_list.append(x)
        else:
            x_list.remove(x)
        if not y in y_list:
            y_list.append(y)
        else:
            y_list.remove(y)
    print(x_list[0], y_list[0])

if __name__ == "__main__":
    main()