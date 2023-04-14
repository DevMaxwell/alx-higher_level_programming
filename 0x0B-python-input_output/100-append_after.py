#!/usr/bin/python3
""" 13. Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ a function that inserts a line of text to a file,
    after each line containing a specific string """

    res = ""
    with open(filename) as r:
        for line in r:
            res += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as inp:
        inp.write(res)
