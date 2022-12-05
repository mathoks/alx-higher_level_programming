#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (len(matrix) == 0):
        print("", end="")
    else:
        for i in matrix:
            for j in i:
                print("{}".format(j), end=" ")
    print()
