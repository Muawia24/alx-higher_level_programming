#!/usr/bin/python3
import sys

if __name__ == "__main__":

    args = len(sys.argv) - 1
    sum = 0

    for i in range(1, args + 1):
        sum += int(sys.argv[i])

    print(sum)
