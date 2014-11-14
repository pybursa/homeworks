import string
import re

def split_sentence(sentence):
    return re.split(r'\s+', sentence)

def count_vowels(word):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    char_list = list(word.upper())
    return sum([''.join(char_list).count(vowel) for vowel in vowels
        if vowel in char_list])

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primes(number):
    return [item for item in range(number) if is_prime(item)]

def get_max_vowels(text):
    sentence = ''.join(ch for ch in text
        if ch not in set(string.punctuation)).split()
    return { word : count_vowels(word) for (word) in sentence }

def get_max_len(text):
    word_list = ''.join(ch for ch in text
        if ch not in set(string.punctuation)).split()
    dict =  { word : len(word) for (word) in word_list }
    max_len = max(dict.values())
    return { key : value for (key, value) in dict.items() if value == max_len }

def reverse_words_and_sentence(sentence):
    PUNCTUATION = set(',.:;?!')
    need_to_captl = list(sentence)[0].isupper()
    words = split_sentence(sentence)
    punctuation = { index : ch for index in range(len(words))
                                    for ch in list(words[index])
                                        if ch in PUNCTUATION }
    reversed_sentence = ' '.join(words[::-1]).lower()
    no_punctuation = ''.join(ch for ch in reversed_sentence
        if ch not in PUNCTUATION)
    rev_words_in_sentc = [word[::-1] for word in split_sentence(no_punctuation)]
    if need_to_captl: rev_words_in_sentc[0] = rev_words_in_sentc[0].capitalize()
    for key, value in punctuation.items():
        rev_words_in_sentc[key] = rev_words_in_sentc[key] + value
    return ' '.join(rev_words_in_sentc)

def reverse(text):
    sentences = re.findall(r"(\S.+?[.!?])(?=\s+|$)", text)
    return ' '.join(reverse_words_and_sentence(sent)
        for sent in sentences[::-1])

def get_info_for_obj(object, spacing = 25):
    """Print methods and doc strings."""
    methodList = [e for e in dir(object) if callable(getattr(object, e))]
    print "\n\n".join(["%s %s" % (method.ljust(spacing),
        ' '.join(str(getattr(object, method).__doc__).split()))
                     for method in methodList])

def get_pseudo_sum(number):
    assert isinstance(number, int) and number > 0
    digits = [int(item) for item in list(str(number))]
    pseudo_sum = 0
    for digit in digits:
        pseudo_sum += digit
    return pseudo_sum
