A = [-4, -1, 0, 3, 10]

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


def sortedSquares(A):
    return sorted(x * x for x in A)


print(sortedSquares(A))
