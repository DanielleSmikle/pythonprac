
# def factorial(n):
#     assert n>=0 and int(n) ==n, 'The number must be postive int only'
#     if n in [0,1]:
#         return 1 
#     else: 
#         return n * factorial(n-1)

# print(factorial(10))


def fib(n):
    assert n>=0 and int(n) ==n, 'fib number cant be neg number or non int like a decimal '
    if n in [0,1]:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))