def ispalindrome(s):
    # D.R.Y.
    from reverse import reverse
    return s == reverse(s)

def main(args):
    print 'is a palindrome' if ispalindrome(args[1]) else 'is not a palindrome'

if __name__ == '__main__':
    import sys
    main(sys.argv)
    