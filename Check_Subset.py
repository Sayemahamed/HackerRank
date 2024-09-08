def main():
    test_case = int(input().strip())
    for _ in range(test_case):
        input()
        a_set = set(map(int, input().strip().split()))
        input()
        b_set = set(map(int, input().strip().split()))
        print(a_set.issubset(b_set))


if __name__ == "__main__":
    main()
