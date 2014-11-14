text_in = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."

def reverse_em(charecter, param = ""):
    text = ""
    formated_text = ""
    for i in (text_in.split(charecter)):
        text += (i[::-1] + " ")
    for j in text.split(' '):
         if '.' in j:
            k = ''.join(((j.replace('.','')), '.'))
            formated_text += (k + " ")
         #elif j[-1].isupper():                    ///Why out of range?
             #k = j.replace(j[-1], j[-1].lower())
         else:
            formated_text += (j + " ")
    return formated_text

def main():
    text_words, text_sentences, text_letters = reverse_em('.'), reverse_em('%s'), reverse_em(' ')

    print "-----Rewersed letters in words------"
    print text_letters

    print "-----Rewersed words in sentences-----"
    print text_words

    print "-----Rewersed sentences in text-----"
    print text_sentences

main()

