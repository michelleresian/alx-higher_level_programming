#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]  # Exclude the script name from the arguments
    num_args = len(args)

    print(f"{num_args}", end=' ')
    if num_args == 0:
        print(".", end='\n\n')
    elif num_args == 1:
        print("argument:", end='\n')
        print(f"{num_args}:", args[0])
    else:
        print("arguments:", end='\n')
        for i, arg in enumerate(args, start=1):
            if i == 0:
                continue
            print(f"{i}: {arg}")


if __name__ == '__main__':
    main()
    