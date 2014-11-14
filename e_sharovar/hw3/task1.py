def getMaxVowelsCount(text):
    vowels = 'aeiouy'
    words = text.split(" ")

    maxCount = 0;

    for word in words:
        count = 0
        for i in word:
            if i.lower() in vowels:
                count += 1
        if count > maxCount:
            maxCount = count

    return maxCount

s = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'
maxVowelsCount = getMaxVowelsCount(s)
print 'Max vowels count:', maxVowelsCount
