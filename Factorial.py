# Python code to demonstrate math.factorial()
import math

print("The factorial of 23 is : ", end="")
print(math.factorial(23))

#########################################
# Python code to demonstrate naive method
# to compute factorial

n = 23
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)

#########################################


def factorial(n):
    # single line code
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


#########################################
# Multiple line code
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


*****************************************
# Iterative code
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact


n = int(input('Check the factorial of:'))
print("Factorial of", n, "is", factorial(n))
