__author__ = 'alex'


def task3_2():
    user_string = "Proin eget tortor risus. Cras ultricies ligula sed magna\
     dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl\
     tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."

    user_list = user_string.replace('.', '').split()
    user_count = []
    for i in user_list:
        sym_count = (i, len(i))
        user_count.append(sym_count)
    res = max(user_count, key=lambda item: item[1])[1]
    result = [tup for tup in user_count if tup[1] == res]
    for i in result:
        print i


task3_2()
