__author__ = 'alex'


def task_1():
    user_input = raw_input("Please, insert a string for reverse: ")

    def reverse_recursive(string):
        if len(string) <= 1:
            return string
        return reverse_recursive(string[1:]) + string[0]

    def reverse_by_loop(string):
        desc_string = ''
        for i in range(len(string)-1,-1,-1):
            desc_string += string[i]
        return desc_string

    print "Variant 1: " + user_input[::-1]
    print "Variant 2: " + ''.join(reversed(user_input))
    print "Variant 3: " + reverse_recursive(user_input)
    print "Variant 4: " + reverse_by_loop(user_input)


task_1()