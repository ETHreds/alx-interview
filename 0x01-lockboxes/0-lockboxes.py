#!/usr/bin/python3
"""
Solution to locked boxes
"""


def canUnlockAll(boxes):
    """
    this function takes an argument and sees
    if all boxes can openned
    List: list
    :return: true or false
    """
    locked_boxes = []
    keys = []
    turn = 0

    for box in boxes:
        if boxes.index(box) == 0:
            continue
        locked_boxes.append(boxes.index(box))
    while turn != 2:
        for box in boxes:
            if boxes.index(box) == 0 or boxes.index(box) in keys:
                if not box:
                    continue
                for key in box:
                    if key not in keys:
                        keys.append(key)
                for key in keys:
                    if key in locked_boxes:
                        locked_boxes.remove(key)
        turn += 1
    if not locked_boxes:
        return True
    return False
