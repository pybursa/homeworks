def max_words(text):
    max_words = [""]

    for word in text.split():
        if len(word) > len(max_words[0]):
            max_words = [word]
        elif len(word) == len(max_words[0]):
            max_words.append(word)
    return " ".join(max_words)

text = '''
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. 
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
'''
print max_words(text)
