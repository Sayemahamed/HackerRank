def main():
    input_count = int(input().strip())
    main_set = set(map(int, input().strip().split()))
    operation_count = int(input().strip())
    for _ in range(operation_count):
        operation = input().strip().split()
        if operation[0] == "intersection_update":
            set_a = set(map(int, input().strip().split()))
            main_set.intersection_update(set_a)
        elif operation[0] == "update":
            set_a = set(map(int, input().strip().split()))
            main_set.update(set_a)
        elif operation[0] == "symmetric_difference_update":
            set_a = set(map(int, input().strip().split()))
            main_set.symmetric_difference_update(set_a)
        elif operation[0] == "difference_update":
            set_a = set(map(int, input().strip().split()))
            main_set.difference_update(set_a)
    print(sum(main_set))


if __name__ == "__main__":
    main()
