#!/usr/bin/python3
"""
Define lockboxes
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    """
    keys = [0]
    for key in keys:
        for vis in boxes[key]:
            if vis not in keys:
                keys.append(val)
    if len(keys) == len(boxes):
        return True
    return False
