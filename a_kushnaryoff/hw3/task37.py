__author__ = 'alex'


def task3_7():
    string_input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." + \
    "Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit " + \
    "amet, consectetur adipiscing elit." + \
    "Donec rutrum congue leo eget malesuada." + \
    "Cras ultricies ligula sed magna dictum porta."

    array_new = []
    array_res = []
    array_last = []

    array = string_input.lower().split('.')
    array.remove('')

    def reverse(string):
        string_new = string[::-1]
        if string_new.startswith(','):
            new_string = string_new[1::1] + ','
            return new_string
        return string_new

    def reverse_sent(list):
        array_result = []
        for d, h in enumerate(list):
            reverse_string_new = reverse(h)
            if d == 0:
                reverse_string = reverse_string_new.capitalize()
            else:
                reverse_string = reverse_string_new
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


task3_7()