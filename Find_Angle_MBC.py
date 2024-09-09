import math


def main():
    AB = int(input())
    BC = int(input())
    AC = math.hypot(AB, BC)
    angle_MBC_radians = math.acos(BC / AC)
    angle_MBC_degrees = round(math.degrees(angle_MBC_radians))
    print(f"{angle_MBC_degrees}°")


if __name__ == "__main__":
    main()
