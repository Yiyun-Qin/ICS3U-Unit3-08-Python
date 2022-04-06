#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, determining whether a year is a leap year or not


def main():
    # This function determines the leap year

    # input
    year_string = input("Please enter the year: ")

    # process & output
    print("")
    try:
        year_integer = int(year_string)
        if year_integer % 4 == 0 and year_integer > 0:
            if year_integer % 100 == 0:
                if year_integer % 400 == 0:
                    print("{} is definitely a leap year!".format(year_string))
                else:
                    print("{} is NOT a leap year!".format(year_string))
            else:
                print("{} is definitely a leap year!".format(year_string))
        else:
            print("{} is NOT a leap year!".format(year_string))
    except Exception:
        print("Invalid answer!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
