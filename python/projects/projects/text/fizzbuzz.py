def fizzbuzz(n):
    fizz = n % 3 == 0
    buzz = n % 5 == 0

    if fizz and buzz:
        return 'fizzbuzz'
    if fizz:
        return 'fizz'
    if buzz:
        return 'buzz'
    else:
        return str(n)

def main(args):
    if len(args) >= 2:
        target = int(args)
    else:
        target = 100

    print '\n'.join([fizzbuzz(n) for n in range(1,target+1)])

if __name__ == '__main__':
    import sys
    main(sys.argv)
    
