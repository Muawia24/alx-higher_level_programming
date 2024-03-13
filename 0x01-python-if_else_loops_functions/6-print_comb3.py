#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j < i or i == j:
            continue
        if str(i) + str(j) != "89":
            print("{}, ".format(str(i) + str(j)), end='')
        else:
            print("{}".format(str(i) + str(j)))
