def main():
    n = int(input())
    first_array = set(map(int, input().strip().split()))
    m = int(input())
    second_array = set(map(int, input().strip().split()))
    print(*sorted(first_array.symmetric_difference(second_array)), sep="\n")


if __name__ == "__main__":
    main()
