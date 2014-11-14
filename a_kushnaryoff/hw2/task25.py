__author__ = 'alex'


def task_25():
    def array_num(array):
        array_odd = []
        array_even = []
        for i, k in enumerate(array):
            if k & 1:
                array_odd.append(k)
            else:
                array_even.append(k)

        array_odd.sort()
        array_even.sort()
        array_new = array_odd + array_even[::-1]

        print array_new

    array25 = [1, 4, 8, 6, 3, 7, 1]
    array_num(array25)

task_25()
