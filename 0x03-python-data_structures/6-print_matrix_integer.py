#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (matrix == undefined):
        print()
    else:
        for i in matrix:
            for j in i:
                print(j, end=" ")
