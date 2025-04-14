#!/usr/bin/env python3

import sys

def fprint(entry: str) -> None:
    print(entry, end='')

num = int(sys.argv[1])

def square(num: int) -> None:
    """Square first line"""
    i = 0
    j = 0
    while (i < num):
        if (i == 0 or i == num - 1):
            fprint("%")
        else:
            fprint("-")
        i += 1
    print()
    """Square middle"""
    x = 1
    while x < num - 1:
        row = 0
        while row < num:
            if row == 0 or row == num - 1:
                fprint("|")
            else:
                fprint(" ")
            row += 1
        print()
        x += 1
    """Square last line"""
    if num > 1:
        i = 0
        while i < num:
            if i == 0 or i == num - 1:
                fprint("%")
            else:
                fprint("-")
            i += 1
        print()

if __name__ == '__main__':
    square(num)