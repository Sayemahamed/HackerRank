def main():
    number=int(input().strip())
    if (number<6 or number>20)and number%2==0:
        print("Not Weird")
    else :
        print("Weird")

if __name__ == '__main__':
    main()