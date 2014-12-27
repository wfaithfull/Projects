def topiglatin(s):
    return ' '.join([wordtopig(x) for x in s.split()])

def wordtopig(w):
    vowels = 'aeiou'

    v = [x for x in w if x in vowels]
    
    if v is None:
        return w

    left, center, right = w.partition(v[0])

    return '%s-%say' % (center + right, left) 

def main(args):
    print topiglatin(' '.join(args[1:]))

if __name__ == '__main__':
    import sys
    main(sys.argv)