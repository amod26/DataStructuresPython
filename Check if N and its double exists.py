arr = [7, 1, 14, 11]

# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).


def checkIfExist(arr):
    tmp = set(arr)
    if 0 in tmp and arr.count(0) > 1:
        return True
    for num in arr:
        if num != 0 and 2 * num in tmp:
            return True
    return False


checkIfExist(arr)
