def empty(deque):
    if len(deque) == 0:
        return 1
    else:
        return 0

def main():
    N = int(input())

    deque = []
    for i in range(N):
        command = input()

        if command == "size":
            print(len(deque))
        elif command == "empty":
            print(empty(deque))
        elif command == "front":
            if empty(deque):
                print(-1)
            else:
                print(deque[0])
        elif command == "back":
            if empty(deque):
                print(-1)
            else:
                print(deque[len(deque)-1])
        elif command == "pop_front":
            if empty(deque):
                print(-1)
            else:
                print(deque.pop(0))
        elif command == "pop_back":
            if empty(deque):
                print(-1)
            else:
                print(deque.pop())
        else:
            command = command.split()
            if command[0] == "push_front":
                deque.insert(0, command[1])
            elif command[0] == "push_back":
                deque.append(command[1])

if __name__ == "__main__":
    main()