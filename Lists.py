def main():
    test_cases = int(input().strip())
    array_list = []
    for _ in range(test_cases):
        command,*temp_list = input().strip().split()
        if command == 'insert':
            array_list.insert(int(temp_list[0]),int(temp_list[1]))
        elif command == 'print':
            print(array_list)
        elif command == 'remove':
            array_list.remove(int(temp_list[0]))
        elif command == 'append':
            array_list.append(int(temp_list[0]))
        elif command == 'sort':
            array_list.sort()
        elif command == 'pop':
            array_list.pop()
        elif command == 'reverse':
            array_list.reverse()


if __name__ == '__main__':
    main()