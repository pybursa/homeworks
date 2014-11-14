# -*- coding: utf-8 -*-
#hw 3/ task1/ Sergei Shybkoi

def count_vowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    res = 0
    for ch in vowel:
        res += string.count(ch)
    return res

def vowel_search(search_string):
    if type(search_string) == str and len(search_string) != 0:
        search_string = search_string.split(' ')
        search_dic = {i: count_vowel(i) for i in search_string}
        sorted_words = sorted(search_dic.items(), key=lambda (k, v): v, reverse=True)
        max_vowel_words = [i for i in sorted_words if i[1] == sorted_words[0][1]]
        print "Vowel's amount in the each word of your text is: \n" + str(search_dic)
        print "Maximum vowels word(s): \n" + str(max_vowel_words)
    else:
        print "You did not enter the text. Try to restart app."


txt = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. " \
      "Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. " \
      "Donec rutrum congue leo eget malesuada. " \
      "fivevowelstest"
vowel_search(txt)
