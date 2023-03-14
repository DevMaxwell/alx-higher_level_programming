#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        #print('here')
        for element in num:
            #print('here too')
            print("{:d} ". format(element), end=" " if element != num[-1] else "")
        print()
