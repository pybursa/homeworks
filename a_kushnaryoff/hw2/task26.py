__author__ = 'alex'


def task_26():
    def sum_key(hsh):
        li = []
        for i, k in enumerate(hsh):
            li.append(str(type(hsh[k]))[7:-2])
        result_dict = {li[i]: li.count(li[i]) for i, k in enumerate(li)}

        print result_dict

    dt = {'a': 1, 3: [1, 5], 'e': 'abc', '6': []}

    sum_key(dt)


task_26()
