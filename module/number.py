def factorial(n=0):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
