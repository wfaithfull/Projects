def collatz(n, count=0):
    if n == 1:
        return count
    if n % 2 == 0:
        return collatz(n/2, count+1)
    else:
        return collatz(n*3+1, count+1)

def main(args):
    print collatz(int(args[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)