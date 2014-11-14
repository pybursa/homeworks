__author__ = 'alex'


def task_23():
    def array_division(array):
        result = {}
        for i, k in enumerate(array):
            if k % 3 == 0:
                result[k] = True
            else:
                result[k] = False

        print result

    list3 = [3, 7, 12]

    array_division(list3)


task_23()
