# classical
def fac(n):
    total = n
    for i in range(n-1,0,-1):
        total = total * i

    return total

# recursive
def facr(n):
    if n == 0:
        return 1
    return n * facr(n-1)

if __name__ == '__main__':
    import sys
    print 'Classical: %d' % fac(int(sys.argv[1]))
    print 'Recursive: %d' % facr(int(sys.argv[1]))