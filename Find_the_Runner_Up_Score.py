def main():
    numbers = int (input().strip())
    arr=  list(map(int, input().strip().split()))
    arr.sort()
    mx = arr[-1]
    for i in reversed(arr):
        if i < mx:
            print(i)
            break
if __name__ == '__main__':
    main()