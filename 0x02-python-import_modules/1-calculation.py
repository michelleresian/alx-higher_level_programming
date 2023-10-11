#!/usr/bin/python3
if __name__ == '__main__':

    from calculator_1 import add, sub, mul, div
    array = [add, sub, mul, div]
    operator = ["+", "-", "*", "/"]

a = 10
b = 5
for i in range(0, len(array)):
    print("{0} {1} {2} = {3}".format(a, operator[i], b, array[i](a, b)))
