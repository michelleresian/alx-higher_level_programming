#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    for i in sys.argv:
        if i != sys.argv[0]:
            add += int(i)
    print("{:d}".format(add))
