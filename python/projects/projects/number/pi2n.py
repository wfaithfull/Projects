# Bailey-Borwein-Plouffe algorithm to calculate arbitrary digits of PI
def bbp(n):
    n -= 1
    x = (4 * sterm(1,n) - 2 * sterm(4,n) - sterm(5,n) - sterm(6,n)) % 1.0
    return '%014x' % int(x * 16**14)

def sterm(j, d):
    # left sum
    left = 0.0;
    k = 0;

    while(k <= d):
        denom = 8*k+j
        left = (left + pow(16, d-k, denom) / denom) % 1.0
        k += 1

    #right sum
    right = 0.0
    k = d + 1
    while 1:
        newright = right + pow(16, d-k) / (8*k+j)
        if right == newright:
            break
        else:
            right = newright
        k += 1
    return left + right

if __name__ == '__main__':
    import sys;
    print bbp(int(sys.argv[1]));