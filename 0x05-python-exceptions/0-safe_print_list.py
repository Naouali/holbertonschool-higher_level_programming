#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    for i in range(x):
        try:
            print(my_list[z], end="")
            z = z + 1
        except IndexError:
            pass
    print("")
    return z
