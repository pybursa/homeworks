__author__ = 'alex'


def task_27():
    def array_num(array):
        def sep(l):
            if len(l) < 2:
                return
            for i in range(len(l)-1):
                j = len(l)-1
                while j > i:
                    if l[j-1] % 2 == 0 and l[j] % 2:
                        tt = l[j-1]
                        l[j-1] = l[j]
                        l[j] = tt
                    elif l[j-1] < l[j] and l[j] % 2 == 0 and l[j-1] % 2 == 0:
                        tt = l[j-1]
                        l[j-1] = l[j]
                        l[j] = tt
                    elif l[j-1] > l[j] and l[j] % 2 and l[j-1] % 2:
                        tt = l[j-1]
                        l[j-1] = l[j]
                        l[j] = tt
                    j -= 1

        sep(array)
        print array

    array27 = [1, 4, 8, 6, 3, 7, 1]
    array_num(array27)

task_27()
