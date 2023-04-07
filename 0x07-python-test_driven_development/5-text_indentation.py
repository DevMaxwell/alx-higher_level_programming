#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ 'print' two new lines after any of ? , or :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    elif text is "":
        print("", end='')
    result = " "
    for i in text:
        if i is result and i is ' ':
            result = i
            continue
        if (result is ':' or result is '.' or result is '?') and i is ' ':
            resut = i
            continue
        if i is '.' or i is '?' or i is ':':
            string += i + "\n" + "\n"
            result = i
        else:
            string += i
            result = i
    print(string.rstrip(' '), end="")
