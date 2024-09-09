from itertools import product


def main():
    set_a = list(map(int, input().strip().split()))
    set_b = list(map(int, input().strip().split()))
    print(*product(set_a, set_b))


if __name__ == "__main__":
    main()
