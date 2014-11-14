__author__ = 'alex'


def task3_3():
    string_input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." + \
    "Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit " + \
    "amet, consectetur adipiscing elit. Donec rutrum congue leo eget" + \
    "malesuada. Cras ultricies ligula sed magna dictum porta."

    array = string_input.replace(',', '').split('.')
    array.remove('')
    array_new = []
    array_res = []

    array_last = []

    def reverse(string):
        string_new = string[::-1]
        return string_new

    def reverse_sent(list):
        array_result = []
        for h in list:
            reverse_string = reverse(h)
            array_result.append(reverse_string)
        return array_result

    for i in array:
        k = i.strip().split()
        array_new.append(k)
    for j in array_new[::-1]:
        array_res.append(j[::-1])

    for m in array_res:
        array_last.append(' '.join(reverse_sent(m)))

    print '. '.join(array_last)


task3_3()