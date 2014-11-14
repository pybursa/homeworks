vowels = ('a', 'e', 'i', 'o', 'u')

user_input = raw_input('Any your string: ')

print len( re.findall('|'.join(vowels), user_input.lower()) )
