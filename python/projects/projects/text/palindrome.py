def ispalindrome(s):
    # D.R.Y.
    from reverse import reverse
    return s == reverse(s)

if __name__ == '__main__':
    import sys
    print 'Is a palindrome' if ispalindrome(sys.argv[1]) else 'Not a palindrome'