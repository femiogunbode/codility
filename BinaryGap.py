# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    gapCounter = 0
    tempCounter = 0
    repeat = False
    binary = list(format(N, "b"))

    for index, digit in enumerate(binary):
        if (digit == '1') and (index == 0):
            pass
        elif digit == '0' and not repeat:
            if index == (len(binary)-1):
                gapCounter = 0
            else:
                gapCounter += 1
        elif (digit == '1') and (index != len(binary)):
            repeat = True
            if tempCounter > gapCounter:
                gapCounter = tempCounter
        elif (digit == '0') and repeat:
            tempCounter += 1
        else:
            pass
    return gapCounter
