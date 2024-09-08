def main():
    set_a_count = int(input().strip())
    set_a = set(map(int, input().strip().split()))
    set_b_count = int(input().strip())
    set_b = set(map(int, input().strip().split()))
    ans = set_a.difference(set_b)
    print(len(ans))


if __name__ == "__main__":
    main()
