__author__ = 'alex'


def task_7(arg):
    def unique_disordered(arg):
        z = set(arg)
        return list(z)

    print 'Not sorted ' + str(arg) + ' == ' + str(unique_disordered(arg))

    def unique_ordered(arg):
        x = set(arg)
        z = list(x)
        z.sort()
        return z

    print 'Sorted ' + str(arg) + ' == ' + str(unique_ordered(arg))


m = ["a", 5, 2, 5, (1, "a"), "a"]
task_7(m)
