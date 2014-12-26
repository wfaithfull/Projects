def reverse(s):
    rev = ''
    for i in range(len(s)-1, -1, -1):
        rev += s[i]
    return rev

def main(args):
    print reverse(args[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)
    