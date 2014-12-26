from text import fizzbuzz, palindrome, reverse, vowelcount, wordcount

def divider():
    print '*' * divlength

divlength = 50
hw = 'hello world'

print 'Fizzbuzz'
print fizzbuzz.main('100')
divider()
print 'Palindrome'
palindrome.main('racecar')
palindrome.main(hw)
divider()
print 'Reverse'
reverse.main('hello')
divider()
print 'Vowel count'
vowelcount.main(hw)
divider()
print 'Word count'
wordcount.main(hw)