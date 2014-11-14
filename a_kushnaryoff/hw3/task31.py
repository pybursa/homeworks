__author__ = 'alex'


def task3_1():
    vowels = ('A', 'E', 'I', 'O', 'U', 'Y')
    user_string = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.\
    Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.\
    Donec rutrum congue leo eget malesuada."

    user_list = user_string.upper().split()
    user_count = []
    for i in user_list:
        vow = sum(1 for t in i if t in vowels)
        user_count.append(vow)
    result = max(user_count)

    print result


task3_1()
