__author__ = 'alex'


def task_29():
    def list_flat(array):
        lists_result = []
        lists_result = sum(array, [])

        print str(array) + " >> " + str(lists_result)

    array = [[1], [4, 8], [6, 3, 7], [1, 3]]

    list_flat(array)


task_29()
