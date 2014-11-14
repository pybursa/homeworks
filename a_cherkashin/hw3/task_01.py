def vowels_again(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    biggest_word = ''
    word_with_max_vowels = {biggest_word: 0}

    for word in string.split():
        vowels_in_word = 0
        for letter in word:
            if letter in vowels:
                vowels_in_word += 1

        if vowels_in_word > word_with_max_vowels[biggest_word]:
            biggest_word = word
            word_with_max_vowels[biggest_word] = vowels_in_word
    return word_with_max_vowels[biggest_word]

text = '''
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus.
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
'''

print vowels_again(text)
