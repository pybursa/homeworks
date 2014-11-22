__author__ = 'o.shestakov'


def cutting(text, limit):
    splitted_text = text.split()
    print splitted_text
    cutted_text = text[:limit]

    print len(cutted_text)
    print cutted_text

    cut_splitted_text = cutted_text.split()
    temp = list()

    for i in range(0, len(splitted_text) - 1):
        if splitted_text[i] != cut_splitted_text[i]:
            # temp.append('...')
            # if i == 0:
            #     temp.append(cutted_text)
            break
        else:
            temp.append(splitted_text[i])

    print " ".join(temp) + "..."

    pass


text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.'

# cutting(text, 6)
