def all_reverse(text):
    sentences = []

    for sentence in text.split("."):
        words = []
        for word in sentence.split(" "):
            words.append(word[::-1])
        sentences.append(" ".join(words[::-1]))

    return ".".join(sentences[::-1])

text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. 
Cras ultricies ligula sed magna dictum porta.'''

print all_reverse(text)
