__author__ = 'alex'


#variant #1
def task_8_1():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
    z = t[2::3]
    print z


#variant #2
def task_8_2():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
    l1 = []
    for i in range(2, len(t) - 1, 3):
        l1.append(t[i])
    print tuple(l1)


task_8_1()
task_8_2()