#!/usr/bin/python3
"""
calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    numOpe = 0
    minOpe = 2
    while n > 1:
        while n % minOpe == 0:
            numOpe += minOpe
            n /= minOpe
        minOpe += 1
    return numOpe