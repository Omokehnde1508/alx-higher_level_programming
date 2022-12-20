#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # variable to keep track of number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()  # print newline after all integers have been printed
    return count
