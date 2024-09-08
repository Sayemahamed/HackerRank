def main():
    person_per_group = int(input())
    room_numbers = list(map(int, input().strip().split()))
    count_set = set()
    probable_set = set()
    for room_number in room_numbers:
        if room_number not in count_set:
            count_set.add(room_number)
            probable_set.add(room_number)
        else:
            probable_set.discard(room_number)
    print(probable_set.pop())


if __name__ == "__main__":
    main()
