#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def perform_operation(a, b, operator):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        return None


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    result = perform_operation(a, b, operator)
    if result is not None:
        print(f"{a} {operator} {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == '__main__':
    main()
