from fractions import gcd

def g(x, n):
    return (x * x + 1) % n

def pollardrho(n):
    x, xfixed, cyclesize, h = 2, 2, 2, 1

    while h==1:
        count = 1
        while(count < cyclesize and h==1):
            x = g(x,n)
            count += 1
            h = gcd(x - xfixed, n)

        if(h!= 1):
            break

        cyclesize = 2*cyclesize
        xfixed = x

    return h

def main(args):
    print pollardrho(int(args[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)