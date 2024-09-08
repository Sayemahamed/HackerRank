def main():
    input_count = int(input().strip())
    numbers = set(map(int, input().strip().split()))
    command_count = int(input().strip())

    for _ in range(command_count):
        command = input().strip().split()
        if command[0] == "pop":
            numbers.pop()
        elif command[0] == "remove":
            numbers.remove(int(command[1]))
        elif command[0] == "discard":
            numbers.discard(int(command[1]))
    print(sum(numbers))


if __name__ == "__main__":
    main()
