def reverse(s):
    rev = ''
    for i in range(len(s)-1, -1, -1):
        rev += s[i]
    return rev

if __name__ == '__main__':
    import sys
    print reverse(sys.argv[1])