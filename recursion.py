import sys
sys.setrecursionlimit(10000)

def factorial(n):
    print(n)
    return n * factorial(n-1)

factorial(3)