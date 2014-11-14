__author__ = 'alex'


def task_5():
    def exemplar(arg):
        return type(arg).__name__

    print 'exemplar(66): ' + exemplar(66)
    print 'exemplar("66"): ' + exemplar("66")
    print 'exemplar(exemplar): ' + exemplar(exemplar)


task_5()