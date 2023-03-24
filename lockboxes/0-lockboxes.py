#!/usr/bin/python3
"""Lockboxes"""
from itertools import dropwhile


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""

    keys = {0}
    rangeboxes = range(len(boxes))

    while True:
        not_found = set()

        for i in rangeboxes:
            if i in keys:
                for key in dropwhile(lambda k: k in keys, boxes[i]):
                    keys.add(key)
            else:
                not_found.add(i)

        if rangeboxes == not_found:
            return False

        if not not_found:
            return True

        rangeboxes = not_found