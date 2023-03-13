#!/usr/bin/python3

#my_list = [1, 2, 3, 4, 5]
def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        print('{:d}'.format(my_list[num]))
