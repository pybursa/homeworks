__author__ = 'alex'


def task_21():

    def square(array):
        if type(array) is list:
            ret = []
            for i in array:
                ret.append(i ** 2)
            print ret
        else:
            ret = []
            for i in array:
                ret.append(i ** 2)
            tup = tuple(ret)
            print tup

    list21 = [1, 2, 3]
    tuple21 = (1, 2, 3)

    square(list21)
    square(tuple21)

task_21()
