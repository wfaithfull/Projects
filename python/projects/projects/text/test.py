import text

def divider():
    print '*' * divlength

divlength = 50
hw = 'hello world'

print 'Fizzbuzz'
print fizzbuzz.main(100)
divider()
print 'Palindrome'
print 'racecar %s' % text.palindrome.main('racecar')
print '%s %s' % (hw, text.palindrome.main(hw))
divider()
print 'Reverse'
print 'hello -> %s' % text.reverse.main('hello')
divider()
print 'Vowel count'
print '%s -> %s' % (hw, text.vowelcount.main(hw))
divider()
print 'Word count'
print '%s -> %s' % (hw, text.wordcount.main(hw))