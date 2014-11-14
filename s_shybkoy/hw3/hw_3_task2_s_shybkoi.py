# -*- coding: utf-8 -*-
#hw 3/ task2/ Sergei Shybkoi

def max_len_search(search_string):
    if type(search_string) == str and len(search_string) != 0:
        search_string = search_string.replace('.', '').split(' ')
        search_dic = {i: len(i) for i in search_string}
        sorted_words = sorted(search_dic.items(), key=lambda (k, v): v, reverse=True)
        max_len_words = [i for i in sorted_words if i[1] == sorted_words[0][1]]
        print "Max length word(s): \n" + str(max_len_words)
    else:
        print "You did not enter the text. Try to restart app."


txt = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. " \
      "Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. " \
      "Donec rutrum congue leo eget malesuada."
max_len_search(txt)

