# fibonacci sequence

# classical
def fib(n):
    a, b = 0, 1
    for i in range(0,n):
        a, b = b, a + b
    return a;

# recursive
def fibr(n):
    if n == 0 or n == 1:
        return n
    return fibr(n-1) + fibr(n-2)

if __name__ == '__main__':
    import sys
    print fib(int(sys.argv[1]))