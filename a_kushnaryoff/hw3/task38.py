__author__ = 'alex'


def task3_8():
    vowels = ('A', 'E', 'I', 'O', 'U', 'Y')
    input = "Cras ultricies ligula sed magna dictum porta. \
    Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. \
    Vestibulum ante ipsum primis in faucibus orci luctus et ultrices  \
    posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, \
    ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, consectetur \
    adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet \
    quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, \
    elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing \
    elit. Sed porttitor lectus nibh."

    user_list = input.upper().replace('.', '').replace(',', '').split()
    vow = 0

    for i in user_list:
        if i.find("A") >= 1 and (i[i.find("A") - 1] not in vowels) and \
                        i.find('A') != (len(i) - 1) and (i[i.find("A") + 1] not in vowels):
            vow += 1
    print vow


task3_8()