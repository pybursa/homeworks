__author__ = 'alex'


def task3_5():
    user_num = raw_input("Please, input a number: ")

    def sum_of_digits(x):
        digits = map(int, str(x))
        sm = 0
        for digit in digits:
            sm += digit
        return sm

    print "sum of the numbers(" + user_num + ") =", sum_of_digits(user_num)


task3_5()
