# suite de Fibonnaci
def fib(n):
    a = 0
    c = 1
    while c < n:
        print(c, end='')
        a, c = c, a+c
    