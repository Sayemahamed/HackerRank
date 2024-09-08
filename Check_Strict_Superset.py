def main():
    main_set = set(map(int, input().strip().split()))
    is_strict_superset = True
    sub_set_count = int(input())
    for _ in range(sub_set_count):
        sub_set = set(map(int, input().strip().split()))
        if not main_set.issuperset(sub_set):
            is_strict_superset = False
    print(is_strict_superset)


if __name__ == "__main__":
    main()
