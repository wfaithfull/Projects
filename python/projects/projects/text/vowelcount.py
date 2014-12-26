def vowelcount(s):
    dict = 'aeiouy'
    count = 0
    for i in range(0,len(s)):
        if s[i] in dict:
            count += 1
    return count

def vowelcountplus(s):
    dict = 'aeiouy'
    # Makes dictionary for histogram style output
    counts = {}
    for v in dict:
        counts[v] = s.count(v)
    return counts

if __name__ == '__main__':
    import sys
    word = sys.argv[1]
    print vowelcount(word)
    for vowel, count in vowelcountplus(word).iteritems():
        print '%s %s] %d' % (vowel, '=' * count, count)