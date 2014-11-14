def getWords(text):
    text = text.replace('.','')
    words = text.split()
    return words

def getMaxLengthWords(words):
    maxLength = 0
    result = []

    for word in words:
        if len(word) > maxLength:
            maxLength = len(word)

    for word in words:
        if len(word) == maxLength:
            result.append(word)

    return result

def printMaxLengthWords(s):
    maxLengthWords = getMaxLengthWords(getWords(s))
    for word in maxLengthWords:
        print word

s = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'
printMaxLengthWords(s)
