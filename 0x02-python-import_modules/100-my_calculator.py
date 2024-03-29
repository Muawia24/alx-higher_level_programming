#!/usr/bin/python3
import sys
import calculator_1 as calc

if __name__ == "__main__":

    args = len(sys.argv) - 1

    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = "+-*/"
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if op == "+":
        cal = calc.add(a, b)
    elif op == "-":
        cal = calc.sub(a, b)
    elif op == "*":
        cal = calc.mul(a, b)
    elif op == "/":
        cal = calc.div(a, b)
    print("{} {} {} = {}".format(a, op, b, cal))
    sys.exit(0)
