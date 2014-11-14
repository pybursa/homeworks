__author__ = 'alex'


def task_28():
    def to_tp(array):
        if len(array) == 1:
            p = (array[-1],)
        elif len(array) == 2:
            p = array[0:2]
        elif len(array) & 1:
            p = zip(*[iter(t)] * 2)
            a = (array[-1],)
            p.append(a)
        else:
            p = zip(*[iter(t)] * 2)

        tp = tuple(p)
        print str(array) + " >> " + str(tp)

    t = (1, 4, 8, 6, 3, 7, 1)

    to_tp(t)


task_28()