
arr = [1, 0, 2, 3, 0, 4, 5, 0]

# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.


def duplicateZeros(__self__):

    n = len(arr)
    i = 0
    while i < n - 1:
        if(arr[i] == 0):
            arr.insert(i + 1, 0)
            i = i + 1
        i = i + 1
    del arr[n:]
    return arr


print(duplicateZeros(arr))
