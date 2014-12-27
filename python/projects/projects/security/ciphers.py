def caesar(msg, amount):
    return ''.join([shift(char, amount) for char in msg])

def shift(char, amount):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not char in alphabet:
        return char

    index = alphabet.index(char) + amount

    while index >= len(alphabet):
        index = index - len(alphabet)

    return alphabet[index]

def usage():
    print 'Usage: ',
    print 'python ciphers.py <shift> <message>' 

def main(args):
    try:
        shift = int(args[1])
        message = ' '.join(args[2:])
        print caesar(message, shift)
    except Exception, e:
        usage()

if __name__ == '__main__':
    import sys
    main(sys.argv)