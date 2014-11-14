# -*- coding: utf-8 -*-

s = "sabrrtuwacaddabra"


def long_alpha(entered_string):
    reslist = []
    reslists = []

    for i in range(entered_string.__len__()-1):
        if reslist.__len__() == 0:
            reslist.append(entered_string[i])
        elif entered_string[i] >= reslist[-1]:
            reslist.append(entered_string[i])
        elif entered_string[i] < reslist[-1]:
            reslists.append(reslist)
            reslist = []
            reslist.append(entered_string[i])
    print reslists
    check_len = 0

    for i in reslists:
        if i.__len__() > check_len:
            check_len = i.__len__()
            result_sequesnce = i
            result = ''.join(result_sequesnce)
    return result

print long_alpha(s)