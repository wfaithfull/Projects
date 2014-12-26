def ispalindrome(s):
    # D.R.Y.
    from reverse import reverse
    return s == reverse(s)

def main(args):
    if ispalindrome(args[1]):
       print 'is a palindrome'  
    else: 
       print 'is not a palindrome'

if __name__ == '__main__':
    import sys
    main(sys.argv)
    