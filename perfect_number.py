#!/usr/bin/env python3
# Created by: Remy Skelton5 program will ask the user for two whole
# min and max and will find all the perfect numbers between them
import math


def main():
    while True:
        # Get the user min and max as a string and display message about program
        print(
            "This program will ask for two whole numbers and it will find all perfect number"
        )
        print("between those two whole numbers and use the same min and max to exit.")
        user_min_str = input("Please enter your min number: ")
        user_max_str = input("Please enter your max number: ")

        # Initialize a flag to check if any perfect numbers are found
        perfect_numbers_found = False

        # Catch if the user min is something wrong
        try:
            # Convert user min as a string to int
            user_min_int = int(user_min_str)

            # Catch if the user max is something wrong
            try:
                # Convert user max as a string to int
                user_max_int = int(user_max_str)

                # if statement for min or max less than 0
                if user_min_int < 0 or user_max_int < 0:
                    print(
                        "\n{}, {} are not positive min and max.".format(
                            user_min_int, user_max_int
                        )
                    )

                # else if statement for min less than 0
                elif user_min_int > user_max_int:
                    print(
                        "\n{}, {} are not valid min and max.".format(
                            user_min_int, user_max_int
                        )
                    )

                # else if statement for valid min and max
                elif user_min_int < user_max_int:
                    # counter loop until max
                    for counter in range(user_min_int, user_max_int + 1):
                        # check if the square root of counter is whole
                        if counter == 0:
                            counter = counter + 1
                        elif math.sqrt(counter) % 1 == 0:
                            print(f"{counter}, ", end="")
                            perfect_numbers_found = True

                    # Case for no perfect numbers found
                    if not perfect_numbers_found:
                        print(
                            f"There are no perfect numbers between {user_min_int} and {user_max_int}"
                        )

                    else:
                        print(
                            f"are all the perfect numbers between {user_min_int} and {user_max_int}\n"
                        )
                # break if user wants
                else:
                    break

            except Exception:
                # Message for invalid user min and max
                print(
                    "\n{}, {} are not a valid min and max.".format(
                        user_min_str, user_max_str
                    )
                )

        except Exception:
            # Message for invalid user min and max
            print(
                "\n{}, {} are not a valid min and max.".format(
                    user_min_str, user_max_str
                )
            )


if __name__ == "__main__":
    main()
