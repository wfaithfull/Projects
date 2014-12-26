# @param n the upper limit of the sieve
def eratosthenes(n):
    nums = range(2,n+1)
    
    # Actual sieving process simply removes numbers divisible by 2, 3, 5 or 7
    # except the numbers themselves.
    for i in 2,3,5,7:
        nums[:] = sieve(nums, i)

    return nums

# This list comprehension trims all values divisible by n, except n itself.
# e.g. sieve([2,3,4,5,6], 2) yields [2,3,5]
def sieve(nums, n):
    return [x for x in nums if x == n or x % n != 0]

def main(args):
    n = int(args[1])
    print ' '.join([str(x) for x in eratosthenes(n)])

if __name__ == '__main__':
    import sys
    main(sys.argv)

