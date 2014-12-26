def vowelcount(s):
    dict = 'aeiouy'
    count = 0
    # Makes dictionary for histogram style output
    hist = {}
    for v in dict:
        hist[v] = s.count(v);
    return (sum(hist.values()), hist)

def main(args):
    word = args[1]
    count, hist = vowelcount(word)
    print 'Total: %d vowels' % count
    for vowel, count in hist.iteritems():
        print '%s %s] %d' % (vowel, '=' * count, count)

if __name__ == '__main__':
    import sys
    main(sys.argv)
    