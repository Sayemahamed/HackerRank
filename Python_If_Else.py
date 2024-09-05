
if __name__ == '__main__':
    n = int(input().strip())
    if (n<6 or n>20) and n%2==0:
        print("Not Weird")
    else :
        print("Weird")