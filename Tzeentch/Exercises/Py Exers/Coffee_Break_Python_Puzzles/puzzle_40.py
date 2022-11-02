#############################
## id 359
## Puzzle Elo 1661
## Correctly solved 60 %
#############################


def fibo(n):
    """Return list containing
    Fibonacci series up to n.
    """
    
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

fib100 = fibo(100)
print(fib100[-1] ==
      fib100[-2] + fib100[-3])
