__author__ = 'alex'


def task_24():
    def array_num(array):
        array_new = []
        if len(array) % 2 == 0:
            for i, k in enumerate(array):
                if k & 1:
                    pass
                else:
                    array_new.append(k)
        else:
            for i, k in enumerate(array):
                if k & 1:
                    array_new.append(k)
                else:
                    pass
        print array_new

    array21 = [3, 7, 12]
    array22 = [3, 7, 12, 7]

    array_num(array21)
    array_num(array22)

task_24()