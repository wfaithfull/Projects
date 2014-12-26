def vowelcount(s):
    dict = 'aeiouy'
    count = 0
    for v in dict:
        count += s.count(v)
    return count

def vowelcountplus(s):
    dict = 'aeiouy'
    # Makes dictionary for histogram style output
    counts = {}
    for v in dict:
        counts[v] = s.count(v)
    return counts

def main(args):
    word = args[1]
    print 'Total: %d vowels' % vowelcount(word)
    for vowel, count in vowelcountplus(word).iteritems():
        print '%s %s] %d' % (vowel, '=' * count, count)

if __name__ == '__main__':
    import sys
    main(sys.argv)
    