#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argsl = len(sys.argv) - 1
    if argsl == 0:
        print("0 arguments.")
    elif argsl == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argsl))
    for i in range(argsl):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
