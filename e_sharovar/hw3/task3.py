s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta.'

def getSentences(s):
    sentences = s.split('. ')
    for sentence in sentences:
        sentence = sentence.replace('.','')
    return sentences

def getWords(text):
    text = text.replace('.','')
    words = text.split()
    return words

def reverseAll(s):

    # reverse sentences
    sentences = getSentences(s)
    sentences.reverse()
    newSentences = []

    for sentence in sentences:

        # reverse words
        words = getWords(sentence)
        words.reverse()
        newWords = []

        for word in words:
            word = word.replace(',','')
            word = word.lower()
            newWords.append(word[::-1])

        # glue words
        newSentence = ' '.join(newWords)
        newSentence = newSentence.capitalize()
        newSentences.append(newSentence)

    # glue sentences
    result = '. '.join(newSentences) + '.'
    return result

print reverseAll(s)
