#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if not type(my_list[i]) == int:
                continue
            print("{:d}".format(my_list[i]), end="")
            count += 1
    except (IndexError, ValueError, TypeError):
        pass
    print()
    return count
