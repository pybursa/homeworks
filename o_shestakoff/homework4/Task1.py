__author__ = 'o.shestakov'


def percentage(text):
    alphabetMap = dict()
    for i in text:
        i = i.lower()
        if i != ' ' and i != '.':
            if alphabetMap.get(i, -1) != -1:
                alphabetMap[i] += 1
            else:
                alphabetMap[i] = 1
    # print alphabetMap
    spaces = text.count(' ')
    dots = text.count('.')
    resLength = len(text) - spaces - dots
    for i in alphabetMap:
        alphabetMap[i] = (alphabetMap[i] / (resLength * 1.0)) * 100

    print alphabetMap
    pass


text = 'Proin eget tortor risus. Cras ultricies ligula sed ' \
       'magna dictum porta. Donec rutrum congue leo eget malesuada.'

percentage(text)
percentage("ABCda")