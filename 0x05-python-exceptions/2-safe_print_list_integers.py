#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_intergers = 0
    for i in range(x):
        try:
            value = my_list[i]
            print("{:d}".format(value), end='')
            printed_integers += 1
        except ValueError:
            pass
        except TypeError:
            pass

        print()
        return printed_intergers
